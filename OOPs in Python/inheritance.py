class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged in!")

class Adminuser(User):
    def __init__(self,username,password,admin_level):
        super().__init__(username,password)
        self.admin_level = admin_level

    def escalate_privileges(self):
        print(f"{self.username} escalted priviledges to level {self.admin_level}")


regular_user = User(username=input("Enter Username: "),password=input("Enter Password: "))
admin_user = Adminuser(username=input("Enter Admin Username: "),password=input("Enter Admin Password: "),admin_level=input("Enter Admin level: "))

regular_user.login()
admin_user.login()
admin_user.escalate_privileges()









                     
      

