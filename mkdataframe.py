import pandas as pd
import numpy as np
import pickle as pkl

'''
    Goal of this program is to process my data from distributing what
    champions users played into a single column and then saving that as a
    pkl file. Using a pkl file because it will retain the types of
    the list of integers as type int and not convert it to string
    as a csv would.
'''

df = pd.read_csv('data/league2016/GoldSummData2016.csv')
df.head()
df = df.fillna(value='0')

user_id = df['SummonerId']

df.drop('SummonerId',axis=1, inplace=True)

df_new = pd.DataFrame()

df_new['champs'] = df['Top'] + ' ' + df['Jungle'] + ' ' + df['Mid'] + ' ' + df['Support'] + ' ' + df['Adc']

size = df_new.shape[0]

for i in range(size):
    df_new['champs'][i] = pd.to_numeric(df_new['champs'][i].split())
    print(i)

pkl.HIGHEST_PROTOCOL = 2

df_new.to_pickle('data/golduserdata.pkl')
