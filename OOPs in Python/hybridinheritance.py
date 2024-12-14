class University(object):
    def __init__(self,uni_name):
        self._uni_name = uni_name

    def showdetails(self):
        print(f"{self._uni_name}")

class Course(University):
    def __init__(self,uni_name,course_name):
        University.__init__(self,uni_name)
        self._course_name = course_name

    def showdetails1(self):
        print(f"{self._course_name}")

class Branch(University):
    def __init__(self,uni_name,branch):
        University.__init__(self,uni_name)  
        self._branch = branch

    def showdetails2(self):
       print(f"{self._branch}")

class Student(Course,Branch):
    def __init__(self,uni_name,course_name,branch,stu_name):
      Course.__init__(self,uni_name,course_name)
      Branch.__init__(self,uni_name,branch)
      self._stu_name = stu_name

    def showdetails3(self): 
        print(f"{self._stu_name}")

class Faculty(Branch):
    def __init__(self,uni_name,branch,fac_name):
     Branch.__init__(self,uni_name,branch) 
     self._fac_name = fac_name

    def showdetails4(self):
        print(f"{self._fac_name}")

s1 = Student("Mewar University","b.tech","cse","harry")
s1.showdetails()
s1.showdetails1()
s1.showdetails2()
s1.showdetails3()

f1 = Faculty("Mewar University","cse","jay sirr")
f1.showdetails4()