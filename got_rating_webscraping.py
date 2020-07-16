import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.imdb.com/title/tt0944947/episodes?season='
seasons = 8
for number in range(1,seasons+1):
    response = requests.get(url+str(number))
    soup = BeautifulSoup(response.content,features='lxml')

    episode_div = soup.find_all('div',attrs={'class':'info'})
    season = soup.find('h3',attrs={'id':'episode_top'}).get_text()
    print(season)

    for episode in episode_div:
        episode_name = episode.find('a',attrs={'itemprop':'name'}).get_text()
        episode_rating = episode.find('span',attrs={'class':'ipl-rating-star__rating'}).get_text()

        print('{} from {} has a {} rating on IMDB.'.format(episode_name,season,episode_rating))
    print('\n')
