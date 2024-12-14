#arithmatic operators
x = 34
y = 45
c = x+y
print("Addition : ",c)#addition
c = x-y
print("Subtraction :",c)#subtraction
c= x/y
print("Division :",c)#Dividion
c=x%y
print("Modulus :",c)#modulus
c=x*y
print("Multiplication :",c)#Multiplication
c=x//y
print("Integer Division :",c)#interger Division
c=x**y
print("Exponent :",c)#exponent


#assignment operators

x = 5 
x+=1
print(x)

#comparision operators
#Result Will be in boolean form

print(3==5) #equal
print(3!=4) #not equal to 
print(3>5) #greater Than
print(3<5) #less than
print(3>=5) #greater than and equal to
print(3<=5) #less Than and equal to

print()
#logical operators
#used to combine conditions

#and operators truth table
#true and true = true
#true and false = false 
#false and true = false 
#false and false = false
print(3<4 and 4<5)
print(3<4 and 4<3)
print(3<4 and 4<5)
print(3<4 and 1<5)

print()
#or operators truth table
#true and true = true
#true and false = true
#false and true = true
#false and false = false
print(3<4 or 4<5)
print(5<4 or 4<3)
print(4<4 or 4<5)
print(2<4 or 1<5)


print()

#not operators truth table
#true and true = true
#true and false = false 
#false and true = false 
#false and false = false
print(not 4<5)
print(not 4<3)
print(not 4<5)
print(not 1<5)

print()

#special operators
#identity operators

#used to compare ids
x = 3
y = x
print(x is y)

print()

a = 1
b = 2
print(a is b) #false
print(a is not b) #true


#membership operators
#in
myString = "python"
print("python" in myString)


print()
#not in 
myString = "python"
print("python" not in myString)
