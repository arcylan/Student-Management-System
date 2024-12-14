#add to list  functions are used to add items to list

li = [1,2,3,4,5,6]
li.extend([7,8,9]) #extend is used to add one or more items to list 
print(li)
li.insert(0,0) #insert is used to  add items at particular point 
print(li)
li.append(10) #append function id used to add  item at last
print(li)

#remove From list functions

li1 = ['hello',9,8,[5,4,6],'python','ruby']
li1.remove([5,4,6]) #whatever we write inside remove function will be removed from the list
print(li1)
li1.pop(4) #same as remove function but we can access it by index
print(li1)
li1.clear() #it will delete all the items in the function
print(li1)