import pandas as pd
import graphlab as gl

pd.__version__


'''
This process is how to get the pickle file in the proper
protocol format such that it can be used by graphlab. The
below code gets the path and loads it into a dataframe.
The dataframe is then converted into an SFrame.
'''

path = 'data/eudata_sparse_protocol_2.pkl'

df = pd.read_pickle(path)

sframe = gl.SFrame(df)
sframe
