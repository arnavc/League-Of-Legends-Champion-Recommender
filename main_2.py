import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, jaccard, cosine
from sklearn.metrics import jaccard_similarity_score
import csv


# --- Load Data --- #
path = '/Users/arnavc/galvanize/capstone/data/util_freq_matrix.csv'
df_main = pd.read_csv(path)

# --- Edit and Subset DataFrame --- #
user_id =df_main['SummonerId']
df = df_main.drop('SummonerId',axis=1,inplace=False)
df_main=df_main[:500]
df=df[:500]

# Placeholder dataframe with item vs item
item_sim = pd.DataFrame(index=df.columns, columns=df.columns)

#Use cosine similarity to fill in columns with values
for i in range(0, len(item_sim.columns)):
    for j in range(0, len(item_sim.columns)):
        item_sim.iloc[i,j] = 1 - cosine(df.iloc[:,i],df.iloc[:,j])

#Placeholder dataframe, to be filled in with closest neighbors
neighbors = pd.DataFrame(index=item_sim.columns, columns = range(1,11))

#Fill in neighbors dataframe with closest similar neighbors from item similarity dataframe
for i in range(0,len(item_sim.columns)):
    neighbors.iloc[i,:10] = (item_sim.iloc[0:,i]).sort_values(ascending=False)[:10].index

#Convert numeric champion id to champion name using dictionary
def champid_to_name():
    path = '/Users/arnavc/galvanize/capstone/data/league2016/ChampId2Name.csv'
    reader = csv.reader(open(path))

    result = {}
    for row in reader:
        key = row[0]
        result[key] = row[1:]

    return result

#Create champion dictionary by calling function above
champ_dict = champid_to_name()

#Copy neighbors dataframe and then make edits on it
neighbors_name = neighbors.copy()

#Replace all numeric champion id's by looping
for col in neighbors_name.columns:
    neighbors_name[col].replace(champ_dict, inplace=True)

#Calculate similarity score
def get_score(history, similarities):
    return (sum(history * similarities) / sum(similarities))

#Placeholder dataframe for similarities
sims = pd.DataFrame(index=df_main.index,columns=df_main.columns)
sims.iloc[:,:1] = df_main.iloc[:,:1]

#Fill in similarity scores
for i in range(0,len(sims.index)):
    for j in range(1,len(sims.columns)):
        user = sims.index[i]
        product = sims.columns[j]

        if df_main.iloc[i][j] == 1:
            sims.iloc[i][j] = 0
        else:
            product_top_names = neighbors.loc[product][1:10]
            product_top_sims = item_sim.loc[product].sort_values(ascending=False)[1:10]
            user_purchases = df.loc[user,product_top_names]

            sims.iloc[i][j] = get_score(user_purchases,product_top_sims)

#Top Champion Scores
sims.head(20)
sims.shape
#Store as csv so dont have to re-calculate during error testing
sims.to_csv('data/base_sim_500user')

#Top champions in champid form
data_recommend = pd.DataFrame(index=sims.index, columns=['user','1','2','3','4','5','6','7','8'])
data_recommend.iloc[0:,0] = sims.iloc[:,0]
for i in range(0,len(sims.index)):
    data_recommend.iloc[i,1:] = sims.iloc[i,:].sort_values(ascending=False).iloc[1:9,].index.transpose()

#Copy DataFrame
data_rec_champ = data_recommend.copy()

#Convert to name
for col in data_rec_champ.columns:
    data_rec_champ[col].replace(champ_dict, inplace=True)
data_rec_champ.head(100)
