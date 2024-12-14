class A:
    def __init__(self,name,age,color):
        self._name = name
        self._age = age
        self._color = color


    def info(self):
        print(f"{self._name} is {self._age} years old and have {self._color} color.")

class B(A):
    def __init__(self,name,eyes,nose,hands,legs,age,color):
        A.__init__(self,name,age,color)
        self._name = name
        self._eyes = eyes
        self._nose = nose
        self._hands = hands
        self._legs = legs

    def bodyInfo(self):
        print(f"{self._name} has {self._eyes} eyes,{self._nose} nose ,{self._hands} hands with {self._legs} legs.")

class C(B):
    def __init__(self,name,eyes,nose,hands,legs,age,color,location):
        B.__init__(self,name,eyes,nose,hands,legs,age,color)
        self._location = location 

    def location(self):
        print(f"{self._name} lives in {self._location}")


ob1 =  C("tom",2,1,2,2,32,"black","delhi")
ob1.location()                     

        

        