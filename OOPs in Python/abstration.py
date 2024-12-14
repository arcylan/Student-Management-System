#Hiding Neccasarry data from code and shows unnesacarry data is know as data abstration.

#Abstract Class :- abstract class is that class which is inherted from ABC , or which have abstract class and concreate class 
#Abstrat Method :- It is that method which only for decoration not for implimentation.


from abc import ABC,abstractmethod

class Vehicle(ABC):  #no object will be created for Abstract class
    @abstractmethod 
    def color(self):
        pass
    def milage(self):
        pass

class Car(Vehicle):
    def color(self):
        print("Coolor = Black")

class Bike(Vehicle):
    def color(self):
        print("color = White")

class Bus(Vehicle):
    def color(self):
        print("color = Blue")                     

class Truck(Vehicle):
    def color(self):
        print("color = Red")

c1 = Car()
b1 = Bike()
Bb1 = Bus()
t1 = Truck()
Bb1.color()
b1.color()


#Access Modifiers/Speifiers :- These are used to make the class or the attribute public protected or private
#in public there is simple written in protected there is one underscore eg (_name) but in private there are two underscores 
#eg (__name) the public attribute can access anyone while protected can be used by the class and derived class but the
#private can only be used within the class the private attribute is decleared.