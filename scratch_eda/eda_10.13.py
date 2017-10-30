import pandas as pd
from collections import Counter

id_pathname = 'data/league2016/SummIds2016.csv'
df_id = pd.read_csv(id_pathname)

df_id.max()
df_id.Rank.unique()

df_id.Rank.value_counts()

#Read data into a dataframe [df]
path_goldsummsdata2016 = 'data/league2016/GoldSummData2016.csv'
df = pd.read_csv(path_goldsummsdata2016)

df.shape
df.head(5)

#Create a new df with Nan values replaced
df_new = df.fillna(value = '0')

#Add new column that totals entries of 5 roles
df_new['champs'] = df_new['Top'] + ' ' + df_new['Jungle'] + ' ' + df_new['Mid'] + ' ' + df_new['Support'] + ' ' + df_new['Adc']
df_new.head(5)
df_new['count'] = ''

for i,j in enumerate(df_new['champs'].head(5)):
    df_new['count'][i] = Counter(list(map(int, j.split())))
df_new['count'].head(5)

'''
    Counts occurences of a champion for a single role. Need to extend this
    to all champs for all users in all roles.
'''
supp_list = df['Support'][3]
type(supp_list)
supp_list
supp = supp_list.split()
type(supp)
a = list(map(int, supp))
type(a)

Counter(a)

# Generalize the process above for the entire data frame









#
