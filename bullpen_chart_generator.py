from collections import defaultdict
from datetime import date, timedelta

import numpy as np
import pandas as pd
import statsapi
from PIL import ImageFont, ImageDraw, Image
from tabulate import tabulate

from constants import TEAMS
from padres_constants import PADRES_STARTERS
from utils import convert_date_to_str, convert_str_to_date, convert_date_to_month_day_str


# returns bullpen ids (minus starters as defined in constants)
def get_scheduled_games_bullpen() -> (date, list[int]):
    scheduled_game_id = statsapi.next_game(TEAMS.San_Diego_Padres.value)
    boxscore = statsapi.boxscore_data(scheduled_game_id)

    if boxscore['teamInfo']['home']['id'] == TEAMS.San_Diego_Padres.value:
        team = 'home'
        opposing_team = 'away'
    else:
        team = 'away'
        opposing_team = 'home'

    scheduled_game = statsapi.schedule(game_id=scheduled_game_id)[-1]
    next_scheduled_game_date_str = scheduled_game['game_date']
    print("Next San Diego Padres game is on {} against the {}".format(next_scheduled_game_date_str,
                                                                      scheduled_game['{}_name'.format(opposing_team)]))

    next_scheduled_game_date = convert_str_to_date(next_scheduled_game_date_str)
    bullpen = boxscore[team]['bullpen']
    bullpen = [pitcher for pitcher in bullpen if pitcher not in PADRES_STARTERS]
    return next_scheduled_game_date, bullpen


def save_text_chart(df: pd.DataFrame):
    sanitized_df = df[df != 0].replace(np.nan, None)
    text_chart = tabulate(sanitized_df,
                          headers='keys',
                          floatfmt=".0f",
                          numalign="right",
                          stralign="right",
                          tablefmt='psql')

    img_width = 2000
    fontsize = 1  # starting font size
    typeface = "consola.ttf"

    font = ImageFont.truetype(typeface, fontsize)
    text_first_line = text_chart.split("\n")[0]
    while font.getbbox(text_first_line)[-2] < img_width:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(typeface, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype(typeface, fontsize)

    print('final font size', fontsize)
    _, _, right, bottom = ImageDraw.Draw(Image.new('RGB', (0, 0))).multiline_textbbox(xy=(10, 10),
                                                                                      text=text_chart,
                                                                                      font=font)
    img = Image.new('RGB', (int(right + 20), int(bottom + 20)))
    d = ImageDraw.Draw(img)
    d.text((10, 10), text_chart, font=font)  # put the text on the image

    img.save("pitch_chart.png")


def fetch_pitch_counts(days=5) -> pd.DataFrame:
    next_scheduled_game_date, relief_pitchers_list = get_scheduled_games_bullpen()

    end_date = next_scheduled_game_date - timedelta(days=1)
    start_date = next_scheduled_game_date - timedelta(days=days)
    games_list = statsapi.schedule(team=TEAMS.San_Diego_Padres.value, start_date=convert_date_to_str(start_date),
                                   end_date=convert_date_to_str(end_date))

    # sanitize games list
    games_list = [game for game in games_list if game['status'] == 'Final' and game['game_type'] == 'R']

    pitch_chart = {d.date(): defaultdict(int) for d in pd.date_range(start=start_date, end=end_date)}

    for game in games_list:
        if game['home_id'] == TEAMS.San_Diego_Padres.value:
            home_away = 'home'
        else:
            home_away = 'away'

        game_date = convert_str_to_date(game['game_date'])

        boxscore_data = statsapi.boxscore_data(game['game_id'])
        for rp in relief_pitchers_list:
            player_stats = boxscore_data[home_away]['players']['ID{}'.format(rp)]
            pitches_thrown = player_stats['stats']['pitching'].get('pitchesThrown', 0)
            pitch_chart[game_date][player_stats['person']['fullName']] += pitches_thrown

    pitch_chart = dict(map(lambda k, v: (convert_date_to_month_day_str(k), v),
                           pitch_chart.keys(), pitch_chart.values()))
    df = pd.DataFrame.from_dict(pitch_chart)

    save_text_chart(df)

    return df
