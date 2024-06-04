# import numpy as np
# import psycopg2
# print("psycopg2 is installed and working!")

import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:12071999@localhost:5432/cc_details'
bd = create_engine(conn_string)
conn = bd.connect()
# print(conn)

# print(df)
# print(df.info)

files = ['customer', 'credit_card']
# dfs = {} 
# for file in files:
df = pd.read_csv('C:\\Users\\hp\\Downloads\\customer.csv')
df1 = df.to_sql('customer', con = conn, if_exists= 'replace', index = False)
    # dfs[file] = d
print(df1)
