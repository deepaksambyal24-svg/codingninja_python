from OOP.inhertance.inheritance_constructors import person


class person:
    def __init__(self)->None:
        print("person constructor")
class student(person):
    def __init__(self)->None:
        super().__init__()
        print("student constructor")
class employee(person):
    def __init__(self)->None:
        super().__init__()
        print("employee constructor")
student = student()
employee = employee()
