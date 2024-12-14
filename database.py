import sqlite3

conn = sqlite3.connect("collage_db")

if conn:
    print("connected")
else:
    print("Not Connected")    

conn = sqlite3.connect("collage_db")

cursor = conn.cursor()

query1 = (''' create table if not exist student(
roll_num int,
name char(100),
dob date,
address char(250),
adhaar_num int          
);
'''
)

cursor.execute(query1)

conn.close()
 
import os
print(os.getcwd()) 