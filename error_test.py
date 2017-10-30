import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
import csv

'''work in progress'''

class Recommender(object):

    def __init__(self, df_util, champ_dict):
        self.df_util = df_util
        self.champ_dict = champ_dict
        self.util_drop = self.df_util.drop('SummonerId',axis=1,inplace=False)
        self.df_item_item = self.util_drop[:50000]
        self.df_user_item = df_util[:500]
        self.df_item_sim = self.df_item_sim()
        self.neighbors = self.neighbors()
        self.neighbor_to_name = self.neighbor_name()
        self.data_similarity = self.data_similarity()
        self.data_rec = self.data_recommend()
        self.data_rec_champ = self.data_to_champ()

    def df_item_sim(self):
        df_item = pd.DataFrame(index=self.df_item_item.columns, columns=self.df_item_item.columns)

        for i in range(0, len(df_item.columns)):
            for j in range(0, len(df_item.columns)):
                df_item.iloc[i,j] = 1 - cosine(self.df_item_item.iloc[:,i],self.df_item_item.iloc[:,j])

        return df_item

    def neighbors(self):
        neighbors = pd.DataFrame(index=self.df_item_item.columns, columns = range(1,11))

        for i in range(0,len(self.df_item_item.columns)):
            neighbors.iloc[i,:10] = (self.df_item_item.iloc[0:,i]).sort_values(ascending=False)[:10].index

        return neighbors

    def neighbor_name(self):
        neighbors_name = self.neighbors.copy()

        for col in neighbors_name.columns:
            neighbors_name[col].replace(self.champ_dict, inplace=True)

        return neighbors_name

    def get_score(history, similarities):
        return (sum(history * similarities) / sum(similarities))

    def data_similarity(self):
        data_similiarity = pd.DataFrame(index=self.df_user_item.index,columns=self.df_user_item.columns)
        data_similiarity.iloc[:,:1] = self.df_user_item.iloc[:,:1]

        for i in range(0,len(data_similiarity.index)):
            for j in range(1,len(data_similarity.columns)):
                user = data_similarity.index[i]
                product = data_similarity.columns[j]

                if self.df_user_item.iloc[i][j] >= .25:
                    data_similarity.iloc[i][j] = 0
                else:
                    product_top_names = self.neighbors.loc[product][1:10]
                    product_top_sims = self.df_item_sim.loc[product].sort_values(ascending=False)[1:10]
                    user_purchases = self.df_user_item.loc[user,product_top_names]

                    data_similarity.iloc[i][j] = get_score(user_purchases,product_top_sims)

        return data_similarity

    def recommend(self):
        data_recommend = pd.DataFrame(index=data_sims.index, columns=['user','1','2','3','4','5','6','7','8'])
        data_recommend.iloc[0:,0] = data_sims.iloc[:,0]

        for i in range(0,len(data_sims.index)):
            data_recommend.iloc[i,1:] = data_sims.iloc[i,:].sort_values(ascending=False).iloc[1:9,].index.transpose()

        return data_recommend

    def data_to_champ(self):
        data_rec_champ = self.data_recommend.copy()

        for col in data_rec_champ.columns:
            self.data_rec_champ[col].replace(self.champ_dict, inplace=True)

        return data_rec_champ

if __name__ == '__main__':
    path = '/Users/arnavc/galvanize/capstone/data/util_freq_matrix.csv'
    df_main = pd.read_csv(path)

    def champid_to_name():
        path = '/Users/arnavc/galvanize/capstone/data/league2016/ChampId2Name.csv'
        reader = csv.reader(open(path))

        result = {}
        for row in reader:
            key = row[0]
            result[key] = row[1:]

        return result

    champ_dict = champid_to_name()

    rc = Recommender(df_main, champ_dict)
    a = rc.df_item_sim()
    b = rc.neighbors()
    c = rc.neighbor_name()
    d = rc.data_similarity()
    rec = rc.data_rec_champ()



    print(a.head(20))
    print(b.head(20))
    print(c.head(20))
    print(d.head(20))
    print(rec)
