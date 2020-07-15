import requests
import pandas as pd
#from requests.auth import HTTPBasicAuth

url = 'https://the-one-api.herokuapp.com/v1/character'

key = 'uyUbjA961tbSNgGcOhNw'

input = {'Authorization': 'Bearer uyUbjA961tbSNgGcOhNw'}


response = requests.get(url,headers = input)

#print(response.json())

df = pd.DataFrame(response.json()['docs'])

#gender_df = df[['name','gender']].copy()

# Change name of typos to 'Male'
df[(df['gender']!='Female') &
    (df['gender'].notnull()) &
    (df['gender']!='Male') &
    (df['gender']!='')] = 'Male'

# Change name of '' to 'No info'
df[df['gender']==''] = 'No info'

# Count per gender
print(df[['name','gender']].groupby(by='gender').agg('count'))
print('\n')

# List of POV characters
pov_list = ['Frodo Baggins','Samwise Gamgee','Bilbo Baggins','Peregrin Took',
'Meriadoc Brandybuck','Aragorn II Elessar','Gandalf','Boromir',
'Gimli','Legolas','Gollum','Saruman','Théoden','Elrond',
'Galadriel','Arwen','Denethor II','Éowyn','Éomer',
'Radagast','Thorin II Oakenshield','Bard','Beorn','Thranduil']

# filter df for pov characters
pov_df = df[df['name'].isin(pov_list)]

# Count pov characters per gender
print(pov_df[['name','gender']].groupby(by='gender').agg('count'))
print('\n')

# Death Count
life_words = ['FO','TA','alive','departed']



# Count deaths on pov population
pov_death_df = pov_df[['name','death']].copy()
deaths = 0
for number in range(len(life_words)):
    deaths += pov_death_df[pov_death_df['death'].str.contains(life_words[number])]['death'].count()

pov_total = pov_df['name'].count()
print('{} deaths on pov population from a total of {}.'.format(deaths,pov_total))


# Count deaths on pov population
# print(pov_df[['name','death']].count())
# print('\n')
#
# print(pov_df[['name','death']])
