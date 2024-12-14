#Student Management System using python and sqlite3 database
import pandas as  pd

#importing tabulate to view result in tabular form 
from tabulate import tabulate

#importing sqlite3
import sqlite3

#creating connection
myConnection = sqlite3.connect("mewar_db.db")

#creating Cursor
myCursor = myConnection.cursor()

#creating Student Table
query = """
create table if not exists student(
roll int,
name varchar(50),
age int,
email varchar(50),
phone char(10)
);
"""
#Execute table query
myCursor.execute(query)

#Creating a function For add the student
def add_student():
    roll = int(input("Enter Student's Roll Number: "))
    name = input("Enter Student's Name: ")
    age = int(input("Enter Student's Age: "))
    email = input("Enter Student's email: ")
    phone = input("Enter Student's Phone Number: ")

#sql query To insert data into tables
    query = f"insert into student values({roll},'{name}',{age},\
'{email}','{phone}')"
    
    #executing the sql query
    myCursor.execute(query)

    #comminting data
    myConnection.commit()

    print("")
    print("Student Added Successfully")
    

#creating a function for information of the student
def student_info():

#creating the sql query to select data
  query = "select*from student;"  

#executing the sql query 
  myCursor.execute(query)
  for record in myCursor:
      print("Records: ",record)
  
#creating a function to search the student
def student_search():
    x = int(input("Enter Student Roll Number To Find: "))

    query = f"select*from student where roll == {x}"
    myCursor.execute(query)
    r = myCursor.fetchone()
    if r:
        query1 = f"select*from student where roll = {x}"
        df =pd.read_sql(query1,myConnection)
        print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
    else:
        print("Wrong Roll Number")
 
#creating a function To update The Student
def update_search():
    x = int(input("Enter  Student Roll Number To Find: "))
    
    query = f"select*from student where roll == {x}"
    myCursor.execute(query)
    
    r = myCursor.fetchone()
    if r:
        y= input("Enter New Phone Number: ")
        query1 = f"update student set phone={y} where roll = {x};"
        myCursor.execute(query1)
        print("")
        print("Student Updated")
       
    else:
        print("Wrong Roll Number") 
        
#creating function to delete the student record 
def delete_student():
    x = int(input("Enter student roll number>>>"))
    
    query = f"select*from student where roll ={x}"
    myCursor.execute(query)
    
    r = myCursor.fetchone()
    
    if r:
        query1 = f"Delete from student where roll = {x};"
        myCursor.execute(query1)
        print("Student record Deleted successfully")
    else:
        print("Wrong student roll number...")

#creating User Interface
while True: #while loop is used to repeat the function untill we exit it
    print("""
+---------------------------------------------+
| MEWAR UNIVERSITY STUDENT MANAGEMENT SYSYEM  |
+---------------------------------------------+
Choose Operation From The Below Options:
1.Add Student
2.Veiw Student
3.Search Student                                                           
4.Update Student
5.Delete Student
6.Exit                    
""")
    choice = int(input("Choose Option You Want To Do: "))
    if choice==1:
        add_student()
    elif choice==2:
        student_info()
    elif choice==3:
       student_search()
    elif choice==4:
        update_search()
    elif choice==5:
         delete_student()
    elif choice==6:
        break
    else:
        print("Invalid Choice...")

import os
print(os.getcwd)