import pandas as pd
from collections import Counter

pathname = 'data/league2016/GoldSummData2016.csv'
df = pd.read_csv(pathname)

df_new = df.fillna(value='0')
df_new['champs'] = df_new['Top'] + ' ' + df_new['Jungle'] + ' ' + df_new['Mid'] + ' ' + df_new['Support'] + ' ' + df_new['Adc']

df_new['count'] = ''

for i,j in enumerate(df_new['champs']):
    df_count['count'][i] = Counter(list(map(int, j.split())))
