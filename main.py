import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, jaccard
from collections import defaultdict
import operator
import csv

class Recommender(object):
    '''The class for the recommender system.
    The things that the class does are as follows:

    1. Create a utility matrix [rows = users, columns = champions]
    2. Calculate user-user similarity between each user. (starting with
    Jaccard similarity, can try cosine if this works)
    3. Cluster users given this similarity
    4. Give recommendations for a user based on the recommendations that
    were give to other users that the initial user was most similar to.

    Arg: takes in dataframe.
    '''

    def __init__(self, df, user_list):
        self.user = df['SummonerId']
        self.df = df
        self.util_matrix = self._util_mat()
        self.user_sim = self.sim_matrix()
        self.user_sim_dict = {}
        self.top_ranked = self.rec()
        self.user_list_idx = self._user_list_to_idx(user_list)
        self.user_sim_of_interest = self.which_user()
        self.champid_to_name = self._champid_to_name()

    def _util_mat(self):
        #Creates a utility matrix which can be used for creating a similarity matrix

        #drop the id column
        self.df.drop('SummonerId', axis=1, inplace=True)

        #store the dataframe as a matrix in X_mat
        X_mat = self.df.as_matrix()

        return X_mat

    def _user_list_to_idx(self, user_list):
        idx_list = []

        for u in user_list:
            idx_list.append((self.user.index[self.user == u])[0])

        return idx_list

    def _user_to_idx(self, listt):
        listtt = []

        for a in listt:
            listtt.append((self.user.index[self.user == a])[0])

        return listtt

    def _champid_to_name(self):
        path = '/Users/arnavc/galvanize/capstone/data/league2016/ChampId2Name.csv'
        reader = csv.reader(open(path))

        result = {}
        for row in reader:
            key = row[0]
            result[key] = row[1:]

        return result

    def sim_matrix(self):
        '''Establish a user-user similarity matrix for a specific user. The
        metric used for this similarity is Jaccard distance.
        '''

        m, n = self.df.shape
        jc_sim = np.zeros((m, m))
        np.diag(jc_sim, 1)

        for i in range(m):
            for j in range(m):
                if i != j:
                    jc_sim[i][j] = (pdist(self.util_matrix[[i, j], :], 'jaccard'))

        return (1 - jc_sim)

    def rec(self):
        #argsort to reorder by the 20 most similar users
        most_sim = np.argsort(-self.user_sim, axis=1)[:, :10]
        a, b = most_sim.shape

        for i in range(a):
            self.user_sim_dict[self.user[i]] = self.user[most_sim[i]].values.tolist()

        top = self.user_sim_dict
        return top

    def which_user(self):
        '''This method grabs the ranking of the users of interest that were
        specified in the user list. It converts all of the rankings from rec
        method into a list of lists and then iterates through user_list_idx.
        While doing so, it creates a new list with rankings for the users
        of interest. It returns a new list with these values.
        '''
        rankings = list(self.top_ranked.values())
        users_of_interest = []
        for user in self.user_list_idx:
            users_of_interest.append(rankings[user])

        return users_of_interest

    def get_champ_rec(self):
        indx = []
        for u_list in self.user_sim_of_interest:
            #convert the list of users to indices, this needs to be done
            #to query the initial dataframe to get frequency counts.
            indices = self._user_to_idx(u_list)
            indx.append(indices)

        champ_list = {}
        for index in indx:
            champ_list[index[0]] = self.get_top_champs(index)

        champ_dict_name = {}
        for key, value in champ_list.items():
            champ_dict_name[key] = self.champid_into_name(value)

        return champ_dict_name

    def get_top_champs(self, index_list):
        user_of_int = index_list.pop(0)
        main_user_champs = (df.loc[user_of_int]).to_dict()
        sort_user = sorted(main_user_champs.items(), key=operator.itemgetter(1), reverse=True)

        champs = []

        for k,v in sort_user:
            if v >= 10:
                champs.append(k)

        list_of_dicts = []
        for i in index_list:
            list_of_dicts.append((df.loc[i]).to_dict())

        dd = defaultdict(list)
        for d in list_of_dicts:
            for key, value in d.items():
                dd[key].append(value)

        summed = {k: sum(v) for (k, v) in dd.items()}
        sort_summed = sorted(summed.items(), key=operator.itemgetter(1), reverse=True)
        champs_entire = []

        for g,h in sort_summed:
            if h>=50:
                champs_entire.append(g)

        recommend_list = list(set(champs_entire) - set(champs))

        return recommend_list

    def champid_into_name(self, champ_list):
        champ_name_list = []

        for c in champ_list:
            champ_name_list.append(self.champid_to_name[c])

        return champ_name_list

if __name__ == '__main__':
    path = '/Users/arnavc/galvanize/capstone/data/util_matrix.csv'
    df = pd.read_csv(path)

    df = df[0:2000]
    user_list = [24984369, 20968379]
    rc = Recommender(df, user_list)
    print(rc.get_champ_rec())
