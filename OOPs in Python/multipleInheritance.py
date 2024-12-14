#Example 1

class OperatingSys(object):
    def __init__(self,name,optimised):
        self._name = name
        self._optimised = optimised

    def manageApps(self):
        print(f"{self._name} Can manage Apps")    

    def quanlity(self):
        print(f"{self._name} is Optimized = {self._optimised}")


class Windows:
    def __init__(self,issecure):
        self._issecure = issecure 

    def feature(self):
        print(f"windows is {self._issecure}")

class lunix(OperatingSys,Windows):
    def __init__(self,name):
        self._name = name

    def usedfor(self):   
        print(f"{self._name} is used for penetration Testing")

O1 = OperatingSys("AppleMacOs","yess")
O1.manageApps()
O1.quanlity()
O2 = Windows("Not So much Secure")
O2.feature()
O3 = lunix("lunix")
O3.usedfor()


#example 2

class Character():
    def __init__(self,name,total_health,damaged_health):
        self._name = name
        self._Total_health = total_health
        self._damaged_health = damaged_health

    def NewHealth(self):   
        print(f"New Health = { self._Total_health - self._damaged_health} ")

class Skills():
    def __init__(self,name,skills_have,skill_level):
        self._name = name
        self._skills_have = skills_have
        self._skill_level = skill_level

    def skills(self):
        print(f"{self._name} have {self._skills_have} skills  at {self._skill_level} level.")   

class Warrior(Character,Skills):
    def __init__(self,name,total_health,damaged_health,skills_have,skill_level,weapon):
        Character.__init__(self,name,total_health,damaged_health)
        Skills.__init__(self,name,skills_have,skill_level)  
        self._weapon = weapon  

    def attack(self):
        print(f"{self._name} attacked with {self._weapon}")


c1 = Character("hitman",total_health=int(input("Enter Total Health = ")),damaged_health=int(input("Enter Damaged Health = ")))
c1.NewHealth()   
c2 = Skills(name=input("Enter Name = "),skills_have=input("Enter Skills Have = "),skill_level=int(input("Enter Skill Level = ")))
c2.skills() 
c3 = Warrior("hitman",100,21,"leadership",3,"ak47")
c3.attack()