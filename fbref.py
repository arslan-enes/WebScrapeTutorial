import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_team_ids(league_id, season):
    leagues = {'12': 'La-Liga',
               '9': 'Premier-League'}
    res = requests.get(f'https://fbref.com/en/comps/{league_id}/{season}/{season}-{leagues[league_id]}-Stats')
    soup = BeautifulSoup(res.text, features='lxml')
    league_stat_table = soup.find("table", {"class": "stats_table"})
    team_ids = {}

    for team_row in league_stat_table.find("tbody").find_all("tr"):
        team_name = team_row.find("td", {"data-stat": "team"}).text.strip()
        team_url = team_row.find("td", {"data-stat": "team"}).a['href']
        team_id = team_url.split('/')[3]
        team_ids.update({team_name: team_id})

    return team_ids


def get_team_player_urls(team_id):
    res = requests.get(f"https://fbref.com/en/squads/{team_id}")
    soup = BeautifulSoup(res.text, features='lxml')
    team_stat_table = soup.find("table", {"class": "stats_table"})
    player_urls = []

    for player_row in team_stat_table.find("tbody").find_all("tr"):
        player_url = player_row.find("th", {"data-stat": "player"}).a['href']
        player_urls.append(player_url)

    return player_urls


def get_player_stats(player_url):
    return pd.read_html(f"https://fbref.com{player_url}")[0]


if __name__ == "__main__":
    # print(get_team_ids('9', '2022-2023'))
    # print(get_team_player_urls('18bb7c10'))
    print(get_player_stats('/en/players/79300479/Martin-Odegaard'))

