from collections import defaultdict
from datetime import date

import pandas as pd
import plotly.express as px

from GameFetcher import unpickle_games, fetch_and_store_games
from constants import teams, divisions


def add_game_record(team_records, winning_team_id, losing_team_id, winning_team_runs=1, losing_team_runs=1):
    team_records[winning_team_id].append(team_records[winning_team_id][-1] + winning_team_runs)
    team_records[losing_team_id].append(team_records[losing_team_id][-1] - losing_team_runs)


def process_game_record(team_records, home_id, away_id, home_score, away_score):
    if home_score > away_score:
        add_game_record(team_records, home_id, away_id)
    else:
        add_game_record(team_records, away_id, home_id)


def generate_standings_chart(fetch_games=False, season=2025):
    if fetch_games:
        fetch_and_store_games(date(season, 3, 1), date(season, 10, 10))

    games = unpickle_games()

    team_records = defaultdict(lambda: [0])
    [process_game_record(team_records, home_id, away_id, home_score, away_score) for
     home_id, away_id, home_score, away_score in
     zip(games['home_id'], games['away_id'], games['home_score'], games['away_score'])]

    record_df = pd.DataFrame.from_dict(team_records, orient='index').transpose()

    record_df = record_df.rename(columns=lambda x: teams[x])  # use full team name for graphing
    fig = px.line(record_df)
    fig.update_traces(hovertemplate=None)
    fig.update_layout(
        title="team record above .500",
        xaxis_title="games played",
        xaxis_range=[0, 162],
        yaxis_title="games above .500",
        # yaxis_range=[-30, 30],
        hovermode="x",
        updatemenus=[
            {
                "buttons": [
                    {
                        "label": division,
                        "method": "restyle",
                        "args": [{"visible": [t['name'] in teams_in_division for t in fig.data]}],
                    }
                    for division, teams_in_division in divisions.items()
                ]
            }
        ]
    )
    fig.show()
