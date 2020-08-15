from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup
params = {}
headers = {}
wins = []
losses = []
years = range(2010, 2020)


def find_number_wins():
    win_number = 0
    for year in years:
        response = requests.get(f'https://www.basketball-reference.com/play-index/tscore.cgi?request=1&match=single&year_min={year}&quarter_is_1=Y&quarter_is_2=Y&quarter_is_3=Y&quarter_is_4=Y&quarter_is_5=Y&team_id=GSW&order_by=pts', params=params, headers=headers)
        html = response.content.decode(response.encoding)
        soup = BeautifulSoup(html, "html.parser")
        score = soup.find_all('td', attrs={'data-stat': 'score_final'})
        for game in score:
            win = game.string
            if 'W' in win:
                win_number += 1
        wins.append(win_number)


def find_number_losses():
    loss_number = 0
    for year in years:
        response = requests.get(f'https://www.basketball-reference.com/play-index/tscore.cgi?request=1&match=single&year_min={year}&quarter_is_1=Y&quarter_is_2=Y&quarter_is_3=Y&quarter_is_4=Y&quarter_is_5=Y&team_id=GSW&order_by=pts', params=params, headers=headers)
        html = response.content.decode(response.encoding)
        soup = BeautifulSoup(html, "html.parser")
        score = soup.find_all('td', attrs={'data-stat': 'score_final'})
        for game in score:
            win = game.string
            if 'L' in win:
                loss_number += 1
        losses.append(loss_number)


find_number_wins()
find_number_losses()
plt.plot(wins, losses)
plt.show()
