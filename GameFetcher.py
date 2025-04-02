import os
from datetime import date

import pandas as pd
import statsapi

from utils import get_str_date

DATA_FOLDER_ROOT = "./data/"
GAMES_DF_FILENAME = os.path.join(DATA_FOLDER_ROOT, "games_df")


def fetch_and_store_games(start_date: date, end_date: date):
    print("fetching games from start date {} to end date {}".format(start_date, end_date))
    # store game results
    # game_id   game_datetime   home_id home_name   home_score   away_name   away_id    away_score
    schedule = statsapi.schedule(start_date=get_str_date(start_date), end_date=get_str_date(end_date))
    schedule = [game for game in schedule if game['game_type'] == 'R' and game['status'] == 'Final']
    games = pd.DataFrame.from_records(schedule, index=['game_id', 'game_datetime'],
                                      columns=['game_id', 'game_datetime', 'home_id', 'home_name', 'home_score',
                                               'away_name', 'away_id', 'away_score'])
    games.to_pickle(GAMES_DF_FILENAME)
    print("stored {} games from start date {} to end date {}".format(len(schedule), start_date, end_date))


def unpickle_games():
    return pd.read_pickle(GAMES_DF_FILENAME)
