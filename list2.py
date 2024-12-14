#list using list() function/class/constructor
li = list([])
li1 = list([34])
li2 = list([45,65,98])
li3 = list(['python','java','ruby'])
li4  = list(['python',45,56.4,4+6j,[2,5,6,]])

print(li)
print(li1)
print(li2)
print(li3)
print(li4)

#slicing in list
print( list(range(1,10)))
print(li4[1:3])
print(li4[::2])

#length of list 
print(len(li4))

#concatinating a list
li5 = li4 + li3
print(li5)

#repeation of list
print(li5*3)

