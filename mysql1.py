#creating Database and showing Database
import pymysql
conn = pymysql.connect(host = "localhost",
                       user= "root",
                       passwd = "arcylan@2101261")
if conn:
    print("connected")
else:
    print("Not Connected")

conn = pymysql.connect(host = "localhost",
                       user= "root",
                       passwd = "arcylan@2101261")
cursor = conn.cursor()

query = "create database hackerrr_db;"
cursor.execute(query)

query1 = "show databases;"
cursor.execute(query1)
for db in cursor:
    print("List Of Database",db)
conn.close()

#creating TABLE inside database

conn = pymysql.connect(host = "localhost",
                       user= "root",
                       passwd = "arcylan@2101261",
                       database = "hackerrr_db")
cursor = conn.cursor()
query = """
create table details(
name char(50),
age int,
sys_hacked int
);
"""
cursor.execute(query)
query1 = "show tables;"
cursor.execute(query1)
for table in cursor:
    print("list of table ",table)
conn.close()

#inserting data in the tables 

conn = pymysql.connect(host = "localhost",
                       user= "root",
                       passwd = "arcylan@2101261",
                       database = "hackerrr_db")
cursor = conn.cursor()
query = """
insert into details values('jai',17,5),
('adam',21,17),
('wett',23,2);
"""
conn.commit()
cursor.execute(query)
query1 = "select * from details;"
cursor.execute(query1)
for row in cursor:
    print("list of Rows ",row)
conn.close()


        