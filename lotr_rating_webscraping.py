import requests
from bs4 import BeautifulSoup
import pandas as pd

url_dict = {'LOTR1':'https://www.imdb.com/title/tt0120737/?ref_=fn_al_tt_1',
    'LOTR2':'https://www.imdb.com/title/tt0167261/?ref_=tt_sims_tti',
    'LOTR3':'https://www.imdb.com/title/tt0167260/?ref_=tt_sims_tti',
    'HOBBIT1':'https://www.imdb.com/title/tt0903624/?ref_=kw_li_tt',
    'HOBBIT2':'https://www.imdb.com/title/tt1170358/?ref_=kw_li_tt',
    'HOBBIT3':'https://www.imdb.com/title/tt2310332/?ref_=kw_li_tt'}
for url in url_dict.values():
    response = requests.get(url)
    soup = BeautifulSoup(response.content,features='lxml')

    # Get movie name
    title_bar = soup.find_all('h1')
    title=''
    for element in title_bar:
        title = element.get_text()

    # Get rating
    rating=soup.find('span',attrs={'itemprop':'ratingValue'}).get_text()

    print('{} has a {} rating on IMDB.'.format(title,rating))
