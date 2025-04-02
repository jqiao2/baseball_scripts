from collections import defaultdict
from datetime import date, timedelta

import dataframe_image as dfi
import pandas as pd
import statsapi

from constants import TEAMS
from padres_constants import PADRES_STARTERS
from utils import get_str_date


def get_scheduled_games_bullpen():
    scheduled_game = statsapi.next_game(TEAMS.San_Diego_Padres.value)
    boxscore = statsapi.boxscore_data(scheduled_game)

    if boxscore['teamInfo']['home']['id'] == TEAMS.San_Diego_Padres.value:
        team = 'home'
    else:
        team = 'away'

    bullpen = boxscore[team]['bullpen']
    bullpen = [pitcher for pitcher in bullpen if pitcher not in PADRES_STARTERS]
    return bullpen


def fetch_pitch_counts(days=5):
    relief_pitchers_list = get_scheduled_games_bullpen()

    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    games_list = statsapi.schedule(team=TEAMS.San_Diego_Padres.value, start_date=get_str_date(start_date),
                                   end_date=get_str_date(end_date))

    # sanitize games list
    games_list = [game for game in games_list if game['status'] == 'Final' and game['game_type'] == 'R']

    pitch_chart = {}
    for game in games_list:
        if game['home_id'] == TEAMS.San_Diego_Padres.value:
            home_away = 'home'
        else:
            home_away = 'away'

        game_date = game['game_date'][5:]  # remove year
        pitch_chart[game_date] = defaultdict(int)

        boxscore_data = statsapi.boxscore_data(game['game_id'])
        for rp in relief_pitchers_list:
            player_stats = boxscore_data[home_away]['players']['ID{}'.format(rp)]
            pitches_thrown = player_stats['stats']['pitching'].get('pitchesThrown', 0)
            pitch_chart[game_date][player_stats['person']['fullName']] += pitches_thrown

    df = pd.DataFrame.from_dict(pitch_chart)

    return df


pitch_count_chart = fetch_pitch_counts()
dfi.export(pitch_count_chart, "reliever_pitch_count_chart.png")
