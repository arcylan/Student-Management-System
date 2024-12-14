#creating Class
class Parrot:
#Defing Attributes
  def __init__(self,name,age,color):
    self.name = name
    self.age=age
    self.color=color
    
#Defining Behavior/Action
  def singing(self):
    print(f"{self.name} is singing a song")

  def dancing(self):
    print(f"{self.name} is dancing") 

  def flying(self):
    print(f"{self.name} is flying")   

  def Age(self):
    print(f"{self.age} year old is {self.name}")  

#creating object
woofy = Parrot("Woofy","8 months","green")
mithu = Parrot("Mithu","6 months","yellow")
pikku = Parrot("Pikku","12 months","orange")

#print woofy details
woofy.singing()
woofy.dancing()
woofy.flying()
woofy.Age()

