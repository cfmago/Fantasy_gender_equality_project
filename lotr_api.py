import requests
import pandas as pd
#from requests.auth import HTTPBasicAuth

url = 'https://the-one-api.herokuapp.com/v1/character'

key = 'uyUbjA961tbSNgGcOhNw'

input = {'Authorization': 'Bearer uyUbjA961tbSNgGcOhNw'}


response = requests.get(url,headers = input)


df = pd.DataFrame(response.json()['docs'])

# Data cleaning
# Change name of typos to 'Male'
df.loc[((df['gender']!='Female') &
    (df['gender'].notnull()) &
    (df['gender']!='Male') &
    (df['gender']!='')),'gender'] = 'Male'

#df.loc[df['gender']=='male','gender'] = 'Male'

# Change name of '' to 'No info'
df.loc[df['gender']=='','gender'] = 'No info'
df.loc[df['gender'].isna(),'gender'] = 'No info'


# Spouse with '' or none will be 'not married'
df.loc[df['spouse']=='','spouse'] = 'Not married'
df.loc[df['spouse'].isna(),'spouse'] = 'Not married'
df.loc[df['spouse']=='None','spouse'] = 'Not married'

# Death Count
life_words = ['FO','TA','alive','departed']

# Creates column Alive with 1 and 0
df['Alive'] = 0
for number in range(len(life_words)):
    df.loc[((df['death'].str.contains(life_words[number])) |
        (df['death'].isna())),'Alive'] = 1




# Total population ----------------------------------------

print('\nTotal population stats:\n')
# Count per gender on Tp
print('Count total characters per gender')
print(df[['name','gender']].groupby(by='gender').agg('count'))
print('\n')

# Count alive on total population
total_df = df['name'].count()
alive_total_df = df[df['Alive']==1]['_id'].count()
print('{} characters alive on total population from a total of {}.\n\n'.format(alive_total_df,total_df))


# Spouse count on total population
#Check for duplicates
# for element in df[df['spouse'].isna()]['_id'].index:
#     if element in df[df['spouse']=='']['_id'].index:
#         print(True)
total_married = df[df['spouse']!='Not married']['_id'].count()

print('{} characters married on total population from a total of {}.\n\n'.format(total_married,total_df))


# Get gender count of people married for total population
print('Married people by gender on total population')
print(df[df['spouse']!='Not married'][['_id','gender']].groupby(by='gender').count())
print('\n')

# Get alived count of people married for total population
print('Alive people by gender on total population')
print(df[df['Alive']==1][['_id','gender']].groupby(by='gender').count())
print('\n')

# Get deaths count of people married for total population
print('People dead by gender on total population')
print(df[df['Alive']==0][['_id','gender']].groupby(by='gender').count())
print('\n')

# POV population ----------------------------------------

print('----------------------------------------')
print('\nPOV population stats:\n')
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

# Count alives on pov population
pov_total = pov_df['name'].count()
alive = pov_df[pov_df['Alive']==1]['_id'].count()
print('{} characters alive on pov population from a total of {}.\n\n'.format(alive,pov_total))

# Spouse count on pov population
pov_married = pov_df[pov_df['spouse']!='Not married']['_id'].count()
print('{} characters married on pov population from a total of {}.\n\n'.format(pov_married,pov_total))

# Get gender count of people married for pov population
print('Married people by gender on pov population')
print(pov_df[pov_df['spouse']!='Not married'][['_id','gender']].groupby(by='gender').count())
print('\n')

# Get alived count of people married for total population
print('Alive people by gender on pov population')
print(pov_df[pov_df['Alive']==1][['_id','gender']].groupby(by='gender').count())
print('\n')

# Get deaths count of people married for total population
print('People dead by gender on pov population')
print(pov_df[pov_df['Alive']==0][['_id','gender']].groupby(by='gender').count())
print('\n')
