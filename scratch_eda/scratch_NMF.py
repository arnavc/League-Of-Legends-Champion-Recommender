from sklearn.decomposition import NMF
import pandas as pd
from sklearn.externals import joblib

df = pd.read_pickle('data/eudata_sparse_protocol_2.pkl')


df[df.sum(axis=1) >10]

sum(df[df.index=='stelar7'])

model = NMF(n_components=10, init='random', random_state=42)

model.fit_transform(df)
joblib.dump(model, 'nmf_model.pkl')


print(model.components_)
print(model.reconstruction_err_)
