#string is the series of chracters or group of collection of orderd characters 
#or 
#anything in single  double  or triple quotes in python is know as string 

#for example 

string = 'hello world'
String = "hello world"
sTring = '''hello world'''

print("this is arcylan's book")
print('my name is "arcylan"')

#it will print as it is 
print('''hello
world''')


print("my first program is",String)

#fast string
print(f"my first program is {String}")

#pythons index starts with 0 even space contains a number
#example
#indexing
sting = "encapsulate"
print(sting[2])
print(sting[8])

#left starts with -1
print(sting[-11])


#slicing syntax

#string[start:stop:step]
#step default is 1

str = "hello world"
print(str[0:5]) #it can be written  as :5
str = "the name is not so good"
print(str[4:9]) #it will print from 4 to 8 

anystr = "you have been checked for penetration"
print(anystr[26:])#start
print(anystr[:3])#stop
print(anystr[::2])#step
print(len(anystr))

myString = "welcome to python"
print(myString[::3]) #step

n1 = 10 
n2 = 20 
n3 = 30

print(f"i am {n1} . i am {n2} and i am {n3}") #using fast string 
print("i am",n1,". i am",n2,"and i am",n3) #without fast string


name = "jhon sall"
age = 68
prof = "SAS software"

print(f"i am {name} .I am {age} years old and i am creator of {prof}")
print("I am",name,".I am",age,"years old and i creator of",prof)

#string in python is immutable(not changable)

#methods for string to manuplicate
#for upper case,lower case,title case,capitalize case,swapcase case.
string = "Welcome to python"
print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())
print(string.swapcase())

#it will find the index value of and string character
print(string.find("c"))

str = "there is rain in spain"
first_i = str.find("i")
second_i = str.find("i",first_i+1)
third_i = str.find("i",second_i+1)
fourth_i = str.find("i",third_i+1)
print(first_i,second_i,third_i,fourth_i)

#example
str = "once there was a drone."
first_e = str.find("e")
print(first_e)
second_e = str.find("e",first_e+1)
print(second_e)
third_e = str.find("e",second_e+1)
print(third_e)
fourth_e = str.find("e",third_e+1)
print(fourth_e)


