#creating tuple using tuple function

t0 = tuple(('python','c++','java'))
print(t0)
print(type(t0))
t1 =tuple((2,4,3,5))
print(t1)
print(type(t1))
t2 = tuple((True,False,True))
print(t2)
print(type(t2))
t3 = tuple((1,2,3,4,'python','hello',(3,4,5,6)))
print(t3)
print(type(t3))

t4 = tuple(range(51,100))
print(t4)

first = t4[9]
print("first =",first)
second =t4[10]
print("second =",second)
third = t4[11]
print("third = ",third)

five = t4[9:14]
print(five)

t7 = (4,5,3,34,[5.5,7.8,7.7])
t7[4][0] = 9
print(t7)

#concatination of a tuple
t9 = (1,2,3)
t10 = (4,5,6)
t11= t9+t10
print(t11)