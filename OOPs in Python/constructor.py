#Constuctor is used to initialize the  objects with attributes
#self is the always the first arugment in constuctor method
#__init__ method 

#THREE TYPES OF CONSTRUCTOR

#Parameterized Constructor
class student:
    def __init__(self,nam,ag,roln,mark):
        self.name = nam
        self.age = ag
        self.roll_numer = roln
        self.marks = mark

ob1=student("tom",18,5,456)
ob2=student("jhon",19,2,345)

print(ob1.__dict__)
print(ob2.__dict__)

#Non-parameterized constuctor
class student:
    def __init__(self):
        self.name = "tom"
        self.age = 24
        self.roll_numer = 23
        self.marks = 65

ob1=student()
ob2=student()

print(ob1.__dict__)
print(ob2.__dict__)

#Default Constructor
class student:
    pass
ob1=student()
ob2=student()

print(ob1.__dict__)
print(ob2.__dict__)

