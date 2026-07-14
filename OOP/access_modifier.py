# data hiding
# it can achieve by  access modifier
class Student:
    # a private member is only accessible within the class
     # it is written as __ and the variable name eg "__phone"  & for protected method  we use single _ score"_"
    def __init__(self,name,marks,phone)->None:
        self.name=name
        self.marks=marks
        self.phone=phone
StudentA= Student("deepak",50,99080980)
print(StudentA.phone)


# to accesh thed phone number cannot access from outside the class is can be done by "private"
#private members are only accessible within the class



def get_aadhar(sel):
    return self.__aadhar
