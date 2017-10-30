import pandas as pd
import numpy as np
import pickle as pkl


df = pd.read_pickle('data/golduserdata.pkl')

df_util = (df.champs).apply(np.bincount).apply(pd.Series)

df_util.drop([0], axis=1, inplace=True)
df_util = df_util.fillna(value=0)

for col in df_util:
    if np.sum(df_util[col]) == 0:
        df_util.drop(col,axis=1,inplace=True)

df_id = pd.read_csv('data/league2016/GoldSummData2016.csv')
user_id = df_id['SummonerId']

df_util = df_util.set_index(user_id)

print(df_util.shape)
print(df_util.head(20))

df_util.to_csv('data/util_matrix.csv')
