#Examle 1 : abnormal termination of code
print("hello world")
print("i am learning python")
try:
 print(12/0) #Exception
except:
 print("zero division not allowed") 
print(12+45)
print("End of code")

#Example 2 : value error or zero division error
try:
 num1 = int(input("Enter First Number>> "))
 num2 = int(input("Enter Second Number>> "))
 print(num1/num2)
except:
 print("Error Occured")

#example 3 : specific exception handle
try:
 num1 = int(input("Enter First Number>> "))
 num2 = int(input("Enter Second Number>> "))
 print(num1/num2)
except ZeroDivisionError:
 print(" Zero Division Error Occured")
except ValueError:
 print("Value Error Occured") 