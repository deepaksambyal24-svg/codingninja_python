#constructor is a class it is called when a object is created
# its pupose is to intialize the intial values
class Student:
    def __init__(self,name)->None:
        print("constructor called")
        self.name=name
studentA=Student("A")       # whenever a object is created constructor is called


# there are two types of constructor  default and parameterized constructor