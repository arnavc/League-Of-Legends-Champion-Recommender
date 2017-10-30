import pandas as pd
import pickle as pkl

df_pkl = pd.read_pickle('data/golduserdata.pkl')

print(df_pkl.head(10))
