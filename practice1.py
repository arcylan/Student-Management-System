#you can extract world from your sentance and identity also

string = input("Enter a sentance or world>> ") #user will write a sentace or word
print(string)
extract = int(input("Enter number you want to extract(starts from 0)>>> ")) #user will type number which he wants to extract
print(extract)
print(string[extract])  #it will print the word which he wants to extract
print(string)
identity = int(input("Enter number whose identity you want>>> "))
print(id(string[identity])) #it will print id of the number typed
string1 = input("Enter Your sentace>>> ")
print(string1)
string2 = input("Enter word Which You want to check in it>>> ")
print(string2 in string1) #it will check wheather the written word is in it ir not
print(string2)

