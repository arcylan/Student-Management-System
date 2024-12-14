#sets are collection of unorderd datatype

#Creating a set
set1 = {2,3,4,2,4,5,6}
set2 = {'python',6.5,6+5j}

#adding items in set
#1) add function

set1.add(10) #it adds only 1 item to set
print(set1)

#2) update function

set2.update('c++','ruby') #it adds more than 1 item to set
print(set2)

#removing items from set

#1)discard function

set3 = {3,43,4,5,5,6}
set3.discard(43) #it removes the item
print(set3) 

#2)remove function
set4 = {4,4,3,5,6,6}
set4.remove(3) #it also removes the item but it gives error when item is already removed
print(set4)

#3)clear function
set5 = {3,5,3,34,5,6}
set5.clear() #it makes the set empty
print(set5)


#Operations

#1)Intersection(&)

set_a = {1,2,3,4,5,6}
set_b = {1,2,3,4,5,6,7,8}

set_c = set_a & set_b
print(set_c)

#2)Union(|)

set_t = {1,2,3,4,5,6}
set_y = {1,2,3,4,5,6,7,8}

set_j = set_t | set_y
print(set_j)

#3)Minus(-)

set_l = {1,2,3,4,5,6}
set_k = {1,2,3,4,5,6,7,8}

set_g = set_l - set_k
print(set_g)
set_m = set_k - set_l
print(set_m)


