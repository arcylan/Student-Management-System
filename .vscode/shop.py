#Creating Table For Data Storage

import sqlite3
myConnection = sqlite3.connect("customer_db.db")
myCursor = myConnection.cursor()

query = """
create table if not exists customer(
name char(50),
parentage char(50),
adhaar_num char(50),
phone char(50),
product_borrowed char(200),
ammout_product int,
amount_paid int,
total_ammount char(50)
);
"""
myCursor.execute(query)

#function For add customer
def add_customer():
 s_no = int(input("Enter Customer ID"))
 name = input("Enter Customer Name: ")
 parentage = input("Enter Customer's Parentage: ")
 adhaar_num = input("Enter Customer's Adhaar Number: ")
 phone = input("Enter Customer's Phone Number: ")
 product_borrowed = input("Enter The Product/s: ") 
 amount_product = int(input("Enter Total Product Amount: "))
 amount_paid = int(input("Enter Amount Paid By Customer: "))
 total_amount = int(print("Total Amount: ",amount_product - amount_paid))
                      

 query = f"insert into customer values('{s_no}''{name}','{parentage}','{adhaar_num}','{phone}','\
{product_borrowed}',{amount_product},{amount_paid},'{total_amount}')"
 myCursor.execute(query)
 myConnection.commit() 

print("")
print("Customer Added Succesfully")

#function to veiw student
def veiw_student():
 query = "select*from customer;"

 myCursor.execute(query)
 for record in myCursor:
    print("Customers :",record)

#function for update customer
def update_customer():
 x =int(input("Enter The Customer's id : "))    
 query = f"Select*from customer where roll == {x}"
 myCursor.execute(query)
 r = myCursor.fetchone()
 if r:
  y = input("Enter Amount Paid: ")
  query1 = f"update student set amount_paid ={y} where roll {x};"
  myCursor.execute(query1)
  print("Customer Updated")
 else:
  print("Wrong Adhaar Number!")

  

    

#creating Menu
while True:
 print("""
+---------------------------------+
| LONE PESTICIDES AND FERTILIZERS |    
+---------------------------------+
|1.Add Customer                   |             
|2.Veiw Customer                  |
|3.Update Customer                |
|4.Search Customer                |            
|5.Delete Customer                |
|6.Exit                           |
+---------------------------------+
""")
 choice = int(input("Enter What You Want To Do: "))
 if choice == 1:
  add_customer()
 elif choice == 2:
  veiw_student()
 elif choice == 3:
  update_customer()
 elif choice == 4:
  pass
 elif choice == 5:
  pass
 elif choice == 6:
  break
 else:
  print("Invalid Choice Please Type Between 1-6: ")
  
