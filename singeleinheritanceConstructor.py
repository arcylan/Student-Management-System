#Base Class
class Vehicle:
    def __init__(self,name,make):
        self.name = name 
        self.make = make

    def vehicle_info(self):
        print(f"Vehicle name :{self.name} and vehicle maker: {self.make}")
#Derived Class
class car(Vehicle):
    def car_info(self):
        print(f"car name : {self.name} and car maker : {self.make}")  

#creating object
car1 = car("Alto","maruti")
car1.car_info()
car1.vehicle_info()

#28-7-2023
