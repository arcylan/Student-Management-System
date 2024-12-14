import pymysql

#creating connecting object 
cnxn = pymysql.connect(host ="localhost",
                       user ="root",
                       passwd = "arcylan@2101261")
if cnxn:
    print("Connected")
else:
    print("Not Connected") 


#creating connecting object 
cnxn = pymysql.connect(host ="localhost",
                       user ="root",
                       passwd = "arcylan@2101261")
#creating cursor
cursor = cnxn.cursor()

#creating databases
query = "create database myOfficeeee_db;"

#creating sql query 
cursor.execute(query)

query1 = "show databases;"

cursor.execute(query1)

for db in cursor:
    print("List of Database",db)

cnxn.close()    
   
#creating table inside border_db
cnxn = pymysql.connect(host ="localhost",
                       user ="root",
                       passwd = "arcylan@2101261",
                       database = "myOfficeeee_db")
#creating cursor
cursor = cnxn.cursor()

#writing sql query

query  = """
create table employeeeee(
name char(50),
age int,
salaray float,
place char(50)
);
"""
#executing sql query 
cursor.execute(query)

query1 = "show tables;"

#executing sql query 
cursor.execute(query1)
for table in cursor:
    print("List of table ",table)

#closing Connection

cnxn.close()    


#creating table inside border_db
cnxn = pymysql.connect(host ="localhost",
                       user ="root",
                       passwd = "arcylan@2101261",
                       database = "myOfficeeee_db")
#creating cursor
cursor = cnxn.cursor()

#writing sql query

query  = """
insert into employeeeee values('a',20,45000,'l'),
('a',26,47000,'p'),
('r',28,43000,'d');
"""

#commiting data
cnxn.commit()

#executing sql query 
cursor.execute(query)

query1 = "select * from employeeeee;"

#executing sql query 
cursor.execute(query1)
for row in cursor:
    print("Rows ",row)

#closing Connection

cnxn.close()    

