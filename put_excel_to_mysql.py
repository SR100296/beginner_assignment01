import sqlalchemy
import pymysql
import pandas as pd

df = pd.read_excel('beginner_assignment01.xlsx')
# print(df)

database_username = 'root'
database_password = 'mysql_pass'
database_ip = 'localhost:3306'
database_name = 'assignment'

database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                      database_ip, database_name))

df.to_sql(con=database_connection, name='excel_data', if_exists='replace')
