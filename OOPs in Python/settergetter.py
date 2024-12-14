# Setter and Getter

class Good:
    def setName(self,nam): #setter : we made a method for setting value here and passed arguments or argument.
        self.name = nam

    def getName(self):
        print(f"The Name Is {self.name}") #gettrt : Here getter is used to fetch the value.


g1 = Good()
g2 = Good()


g1.setName("jayy") # we set the value of the argument which we passsed in set  method above. 
g2.setName("huhrr") # same 

print(g1.__dict__) #we call the set method and checks the result wheather the value is setted ot not.
print(g2.__dict__)

g1.getName() # we try to call the get method just to fetch the values only.
g2.getName()