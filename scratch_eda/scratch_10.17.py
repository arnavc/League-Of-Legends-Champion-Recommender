rimport mysql.connector as sql
import pandas as pd
import pickle as pkl

pd.__version__

db_connection = sql.connect(host='localhost', database='euplayerdata', user='root')

df_sql = '''
            SELECT
                s.name AS summonername,
                p.championid,
                COUNT(p.championid) AS timesPlayed
            FROM
                participants p
                    JOIN
                participantidentity pi ON p.id = pi.participant
                    JOIN
                summoners s ON pi.summoner = s.id
            WHERE
                platformid LIKE 'euw1'
            GROUP BY s.summonerid, p.championid
            ORDER BY timesPlayed DESC
        '''

df = pd.read_sql(df_sql, con = db_connection)

#making a pickle file of base data
pkl.HIGHEST_PROTOCOL = 2

df.to_pickle('data/eubaserecommender.pkl')

for row in df.head(5).iterrows():
    print(row[1][0])


df.shape
df.head(5)

len(df['summonername'].unique())

len(df['championid'].unique())

df['championid'].unique()

df_sparse = pd.DataFrame(data=0, index=df['summonername'].unique(), columns=df['championid'].unique())

df_sparse

for row in df.iterrows():
    df_sparse.loc[row[1][0],row[1][1]] = row[1][2]

df_sparse.shape

pkl.HIGHEST_PROTOCOL = 2


#convert picklefile to protocol 2 for use in graphlab
df_convert = pd.read_pickle('data/eudata_sparse.pkl')
df_convert.to_pickle('data/eudata_sparse_protocol_2.pkl')


a = 'hi my name is'
b = 'jeff'
c = ' i hate memes'





#
