#string data type

str = "what is your name ?"
#slicing
print(str[::2])
print(str[3:])
print(str[:4])
#indexing
print(str[0])

#some cases
print(str.upper())
print(str.title())
print(str.lower())
print(str.swapcase())
print(str.capitalize())


#find case
str1 = "death keeps no calender"
first = str1.find("e")
print(first)
second = str1.find("e",first+1)
print(second)
third = str1.find("e",second+1)
print(third)
fourth = str1.find("e",third+1)
print(fourth)
fifth =str1.find("e",fourth+1)
print(fifth)



