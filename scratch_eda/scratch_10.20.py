import pandas as pd
import math
import numpy as np

'''
    This entire program did not achieve what the goal was. The goal was
    to be able to create a new dataframe that had the champs played as
    a list of integers. It did it for a single case but was not able to
    do it and then appropriately save it to a file. Probably had something
    to do with the way the new dataframe was created -> poor creation because
    I initialized it to was bad'''

pathname = 'data/league2016/GoldSummData2016.csv'
df = pd.read_csv(pathname)

user_id = df['SummonerId']

df.drop('SummonerId', axis=1, inplace=True)

df1 = df.fillna(value='0')

df_new = pd.DataFrame(data=0, index=user_id, columns=['champs'])

df1['champs'] = df1['Top'] + ' ' + df1['Jungle'] + ' ' + df1['Mid'] + ' ' + df1['Support'] + ' ' + df1['Adc']

for i in range(df1.shape[0]):
    df_new.champs[i] = list(map(int, df1['champs'][i].split()))
    print(i)


df_new.to_csv('/Users/arnavc/galvanize/capstone/df_new.csv')
