# OOPS : ---> OBJECT ORIENTED PROGRAMMING
from pyexpat import model

account_number ='a101'
balance=10000
def deposit(balance , amount):
    balance=balance+amount
    return balance
def withdraw(balance , amount):
    balance=balance-amount
    return balance

# object -oriented --organizing instructions around objects
# progammring --instructions given to computer
# object -- data  and actions

# data - --> attributes
# actions --- > methods ,withdrawal ---> methods
# procedural programming vs oop ---> what steps /functions should the program perform
# OOP --> What objects exist in the problem i
# object --> customer ,account,employee, loan , transaction
# then we ask what information and actions belong to each object

# why we need oop ?
#1)  managing complexity
# 2) reusability
# 3) book dvd ,
# library system ---- book ,member, librarian , transaction

class libraryitem:
    def __init__(self,balance , amount):
        self.title=title
        self.balance=balance
        self.amount=amount
class book (libraryitem):
    pass

#extensibiltiy can i easily add something new to the program

# classes and objects
# class are the blue print /template used to create objects

class car :
    def __init__(self,make,model,year):
            self.make=make
            self.model=model
            self.year=year

# init -----> constructor method used to intialise the objects attribute

# self -----> thisparticular object
car1=car("toyota","camry",2020)
car2=car("honda","mango",2021)

# attributes : -----> variables belonging to an object
print(car1.make)
print(car2.model)


# methods ----> all functions that belongs to a particular class
class car:
    def start(self):
        print("car start")
#attribute ------> what an object does


# creating objects
class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

car1=car("toyota","mango",2020)
car2=car("honda","mango",2021)
# dot----> to access a property inside a class

# class attribure vs instance attribute

class car:
    wheels=10  # class attributes


# instance attributes -- make model , year  they differ from object to object


# library management system


# objects --> books ,member , librarian ,
# attributes --. title, author , ISBN , checkout checked_id
#methods of book ----> check_out , check_in

class book:
    def __init__(self,title,author,ISBN):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.checked_out=False



# member class ---> member_object ---> it borrow book () action , book object

# inheritance ----> reuse parent children
# polymorphism ---->many forms
# encapsulation----> protect
# abstraction-----> hide complexity

# inheritance ----->
class vehicle :
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

class car(vehicle):
    def __init__(self,make,model,year):
        vehicle.__init__(self,make,model,year)
# parent class and child class

# vehicle ---> parent class m base class , superclass
# car --> child class derived class subclass


# super() --->
class car(vehicle):
    def __init__(self,make,model,year,num_doors):
        super().__init__(make,model,year)
        self.num_doors=num_doors


# method overriding :
class vehicle :
    def start(self):
        print('starting the vehicle ')
class car(vehicle):
    def start(self):
        print('start with a key')
class bike(vehicle):
    def start(self):
      print('start with a button ')
# why inhertiance
# code reuse
# organized
# maintain

#polymorphism---> methods is same beganbe changes Think of a Smartphone.
# It has a single button or command called "Take a Photo."If you activate the
# standard camera, it captures a regular photo.If you switch to the ultra-wide
# lens, the same command captures a wide-angle photo.If you switch to portrait mode,
# the exact same command creates a blurred-background photo


# shape --circle , rectangel ---area
# why oplymorphism

# flexibility scalability   maintainability


# encapsulation ---> protecting the data
# private attributes ----> self .__balance __.__ double under score is the method or make attribute private


def deposit(self,amount):
    if amount>0:
        self.__balance+=amount

# data protection controlled access code maintenance


# getter and setter :
# getter ---> get .read a value
# setter --> set change a value
class person :
    def __init__(self,first_name,last_name,age):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__age=age

    def get_name(self):
        return self.__first_name
    def get_age(self):
        return self.__age
person1=person("john","doe",18)
print(person1.get_name())
print(person1.get_age())
def set_name(self,name):
    if name!=" ":
        self.__first_name=name


# abstraction  ---->
# abstract method

class person(person):
    @abstractmethod
    def __init__(self,first_name,last_name,age):
        person.__init__(self,first_name,last_name,age)
