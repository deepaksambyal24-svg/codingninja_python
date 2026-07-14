  # divisionby zero clas is inhertied from exception base class
    # so in tuple we have write the exception class
    # __init__ is the constructor
    # and super() is the consturctor for  base class
class DivisionByZeroException(Exception):
    def __init__(self)-> None:
        print('division by zero')
        super().__init__()
a=10
b=0

if b==0:
    raise DivisionByZeroException()             # we have raise the exception

num=a/b


# encapsulate inside the method
def perform_operation(a,b):
    if b==0:
        raise DivisionByZeroException()
    num=a/b
a=10
b=0
try:
    perform_operation(a,b)
except DivisionByZeroException:
    print("division by zero")