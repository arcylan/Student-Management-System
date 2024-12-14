#polymorphism is having same function but doing different tasks:
#1) Method Overloading 2) Method Overidding 3) duck typing 4) operator overloading


#Method Overloading
class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print(f"Area of reactangle = {a*b}")
        elif a!=None:
            print(f"Area of Square = {a*a}")
        else:
            print("Nothing")

ob = Area()
ob.find_area()
ob.find_area(10)
ob.find_area(10,20)


#Method Overridding
class Laptop:
    def func(self):
        print("laptop")
class Mobile(Laptop):
    def func(self):
        print("Mobile")
        super().func()
ob = Mobile()
ob.func()        

#method overridding eg+

class Car():
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def ss(self):
        print(f"{self.name} is in  {self.color} color")

class Bus(Car):
    def ss(self):
        super().ss()
        print("This message is from Bus class")


o = Bus("alto","black")
o.ss()



















