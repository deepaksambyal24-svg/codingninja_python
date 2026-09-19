# database connectivity :
# phthon application --- python program

# pyhon application ---> database connector , database --> python application

# reasons for data base connectivity :
# 1) data storage and management
# 2) Data retrival and manipulation _( how we can access data)
# 3) concurrent access  --- happening at the same time
# 4) security   ----> only authorised people can handle the database
# 5) scalability-----> database application can handle increasing data and user demand as the system grows

# # LIBRARIES FOR DATABASE CONNENCTIVITY
# PSYCONPG2---> USED FOR FOCNNECTING PYTHON WITH POSTGRESQL DATABASE
# 2) SQLALCHEMY

# IMPORTANT TERMS : ----
# conn ---. connection ( opens the communication with the data base
# cursor ---> execute sql commands thourgh that connection
# connection ---> telephone connectio
# curosr ---> person speaking
# sql query --> message between the two people

# fetchchall () --- retrieve the required rows
# cur.close () , conn.close () -- reequired to close the connection
 # flow of connection --> connect --> create cursor --> execute sql --> fetch results --> close cursor --> close connection

from sqlalchemy import create_engine
# sqlalcheny higher level interface and inclueds ORM ( OBJECT RELATIONAL MAPPER )
# IT is used to provide  both ORM and sql toollkit capabilities while supporting multiplle database
# psycomp2:
# flow : python --> sql queries --> postgesql
# slalchemy ORM
# FLOW : PYTHON ---> PYTHON CLASS /OBJECTS ---> database

# orm
# objects in data ---> table row column
# object in python ---. class , object , attirbute

# sqlalchemy engine : --->
from sqlalchemy import create_engine
import psycopg2
# psycopg2 ---> lower level , mainly posgresql , direct sql is common, cursor base interaction
# sqlalchemy ---> higher level , multiple databases , ORM CLASS CAN BE USED , ENGINE SESSION ./MODEL APPROACH
# CONNECTION DETAILS   :

# HOST ___LOCAL HOST , PORT -- 3306 USER NAME --. ROOT AND PASSWORD
import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="6995",database="health")
print("connecting successfuly")
if connection.is_connected():
    print('python is conencted to mysql ')
else:
    print('python is not connected to mysql')

# create a cursor
# cursor --> sending sql commands to python and sql to and from

cursor=connection.cursor()
cursor.execute("select * from healthcare")
rows = cursor.fetchall()

for row in rows:
    print(row)

import pandas as pd


# second method load my sql into pandas
cursor.execute("select * from healthcare")
rows = cursor.fetchall()
columns=[col[0] for col in cursor.description]
df = pd.DataFrame(rows,columns=columns)
print(df)

cursor.execute("select * from healthcare")
rows = cursor.fetchall()
for r in rows:
    print(r)


# filtering the data
query='''select * from healthcare where  patient_name ="Aditya Das"'''
cursor.execute(query)
rows = cursor.fetchall()
columns=[col[0] for col in cursor.description]
it_df=pd.DataFrame(rows,columns=columns)
print(it_df)


print(it_df["visit_fee"].mean)

cursor.execute("select * from healthcare")
rows=cursor.fetchall()
columns=[col[0] for col in cursor.description]
df=pd.DataFrame(rows,columns=columns)
print(df.T)
print(df.groupby("appointment_status").count())

