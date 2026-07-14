class person(object):
    def __init__(self,name,age,idno)->None:
        self.name = name
        self.age = age
        self.idno = idno
    def walk(self):
        print("walking")
    def eat(self):
        print("eating")
class employee(person):
    def __init__(self,empno,team):
        self.empno = empno
        self.team = team
    def work(self):
        print("working")
        # here we should be able to initialise the person as well
        # by using the super keyword
        # to access the base class within the derived class by keyword SUPER 
        super().__init__(self.empno,self.team)
    def eat(self):
        print(f"{self.empno} eating")
    def attendance(self):
        print(f"{self.empno} attendance")

emp = employee("James",1)
emp.walk()