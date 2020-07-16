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
print('Count total characters per gender')
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
print('Count pov characters per gender')
print(pov_df[['name','gender']].groupby(by='gender').agg('count'))
print('\n')

# Death Count
life_words = ['FO','TA','alive','departed']

# Count deaths on total population
total_alive_df = df[['name','death']].copy()
alive = 0
for number in range(len(life_words)):
    alive += total_alive_df[total_alive_df['death'].str.contains(life_words[number]) |
    total_alive_df['death'].isna()]['death'].count()

df_total = df['name'].count()
print('{} characters alive on total population from a total of {}.\n\n'.format(alive,df_total))


# Count alives on pov population
pov_alive_df = pov_df[['name','death']].copy()
alive = 0
for number in range(len(life_words)):
    alive += pov_alive_df[pov_alive_df['death'].str.contains(life_words[number])]['death'].count()

pov_total = pov_df['name'].count()
print('{} characters alive on pov population from a total of {}.\n\n'.format(alive,pov_total))

# Spouse count on total population
#print(df[df['spouse']=='']['_id'].index)
#print(df[df['spouse'].isna()]['_id'].index)

#Check for duplicates
# for element in df[df['spouse'].isna()]['_id'].index:
#     if element in df[df['spouse']=='']['_id'].index:
#         print(True)
total_married = df[df['spouse']=='']['_id'].count() + df[df['spouse'].isna()]['_id'].count()
print('{} characters married on total population from a total of {}.\n\n'.format(total_married,df_total))


# Spouse count on pov population
pov_married = pov_df[pov_df['spouse']=='']['_id'].count() + pov_df[pov_df['spouse'].isna()]['_id'].count()
print('{} characters married on total population from a total of {}.\n\n'.format(pov_married,pov_total))


# print('-----')
# print(pov_df[pov_df['spouse'].isna()]['_id'].count())
# print(('-----'))
# print(pov_df[pov_df['spouse']=='']['_id'].count())
# #print(pov_df['spouse'])
# print('-----')
# print(df[df['spouse'].isna()]['spouse'])
# print('-----')
# print(pov_df[['name','spouse']])
