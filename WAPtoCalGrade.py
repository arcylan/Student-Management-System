while True:

   hindi = float(input())  
   Maths = float(input())   
   Science = float(input())   
   SST = float(input())   
   sanskrit = float(input())  
   per_marks = (hindi+Maths+Science+SST+sanskrit)*500/100

   if per_marks>=95:
       print("Grade A")
   elif per_marks>=75 and per_marks>=95:
       print("Grade B")
   elif per_marks>=55 and per_marks>=75:
       print("Grade C")
   elif per_marks<55:
       print("Grade D")
   else:
       print("Invalid Choice")
       
       response = input(""" IF YOU WANT TO CALCULATE AGAIN 
    PRESS : Y
    IF YOU WANT TO EXIT 
    PRESS : N""")
   if response.upper() =="N":
       break       
                  
