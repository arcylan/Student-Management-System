#snytax of parent to child class

# class BaseClass:
#     body of the base class
# class DerivedClass(BaseClass):
#     body of the Base class

#single Inheritance

#Base Class
class Vehicle:
    def vehicle_info(self):
        print("inside Vehicle Class")
#Derived Class
class car(Vehicle):
    def car_info(self):
        print("Inside of car class")  

#creating object
car1 = car()
car1.car_info()
car1.vehicle_info()

print("")
print("")



