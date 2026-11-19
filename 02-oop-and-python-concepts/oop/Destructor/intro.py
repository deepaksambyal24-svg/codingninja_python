# it called when a class is deleted in python there is automatically garbage collection
# so we dont need to call it
class Student:
    def __init__(self,name,age)->None:
        self.name=name
        self.age=age
    # to use destructor we use __del__ in place of __init__
    def __del__(self)->None:
        print("destructor called")

studenta=Student("A",24)
del studenta #  destructor is called on this

