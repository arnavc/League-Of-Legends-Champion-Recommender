import pandas as pd
import numpy as np

path = '/Users/arnavc/galvanize/capstone/data/util_matrix.csv'
df = pd.read_csv(path)

df.head()
df.describe()
df.head()
user_id = df['SummonerId']
df.drop('SummonerId', axis=1,inplace=True)
df.head()

#take total across the entire row and create a new column with Total
df['Total'] = df.sum(axis=1)
df.head()

#get frequency of each row by taking the value and dividing it by the total column
df_new = df.loc[:,'1':'432'].div(df['Total'], axis=0)

#get format into the right one for util matrix with index as SummonerId
df_new = df_new.set_index(user_id)

#store the utility frequency matrix to csv for easy access later
df_new.to_csv('data/util_freq_matrix.csv')
