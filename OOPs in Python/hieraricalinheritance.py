class Human():
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def printt(self):
        print(f"{self._name} is {self._age} years old!")

class Male(Human):
    def __init__(self,name,age,gender):
        Human.__init__(self,name,age)
        self._gender = gender

    def show(self):
        print(f"{self._name} is {self._gender}!")


class Female(Human):
    def __init__(self,name,age,location):
          Human.__init__(self,name,age)
          self._location = location

    def show1(self):
        print(f"{self._name} lives in  {self._location}!")

ob1 = Male("tom",21,"male") 
ob1.show()    
ob1.printt()
ob2 = Female("hina",34,"delhi")
ob2.show1()
ob2.printt()

