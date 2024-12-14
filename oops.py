class player:
    name = "Hitman"
    id = 21232425
    age = 21
    FD = 4.1

    def info(self):
      print(f"{self.name} with id {self.id} at the Age of {self.age} has FD of {self.FD}")


a = player()
b = player()
c = player()
d = player()

a.name = "Ghost"
a.id = 21232426
a.age = 22
a.FD = 3.5

b.name = "venom"
b.id = 21232427
b.age = 20
b.FD = 5.1

c.name = "spidy"
c.id = 21232428
c.age = 26
c.FD = 2.6

d.name = "killerrr"
d.id = 21232429
d.age = 24
d.FD = 3.0

a.info()
b.info()
c.info()
d.info()