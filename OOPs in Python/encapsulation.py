#Wrapping Up of data members and methods in a single unit is know as encapsulation.
class Human():
    def __init___(self,name,age):
        self.__name = name
        

    def get_name(self):
        return self.__name
        

    def  set_name(self,name):
        self.__name = name   

    def show(self):
        print(f"{self.__name} 34 years old")

h1 = Human()
h1.set_name("oooo")  
print(h1.get_name()) 
h1.show()         