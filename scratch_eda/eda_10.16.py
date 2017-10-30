import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='localhost', database='euplayerdata', user='root')

sql_1 = 'SELECT * FROM matches LIMIT 10'
df1 = pd.read_sql(sql_1, con=db_connection)
df1
sql_2 = '''
            SELECT *
            FROM avg_stats
            LIMIT 100
        '''
df2 = pd.read_sql(sql_2, con=db_connection)
df2

df3 = pd.read_sql('SELECT )
