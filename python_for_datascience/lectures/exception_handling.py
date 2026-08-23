# EXCEPTIONS HANDLING ---->
from scipy.cluster import hierarchy

from revision import error

# RECURSION :----> A function calls itself again and again until a base condition is met.
# or a untill a stopping condition is met. Recursion is a programming technique where a
# function calls itself to solve a smaller instance of the same problem.
# It is often used to solve problems that can be broken down into smaller, similar subproblems.

#total sales for 5 days =today's sales of remaining 4 days


# it has two parts
# base condition
# recursive call
# syntax

# def funtion_name(value):
#               return result
#           return funtion_name(value-1)  # recursive call

# total daily sales

sales=[12000,15000,10000,18000,20000]
def total_sales(data):
    if len(data)==0:
        return 0
    else:
        return data[0]+total_sales(data[1:])
result=total_sales(sales)
print(result)

#   calculate employee hierarchy level


#   CEO---> DIRECTOR ----> MANAGER ----> EMPLOYEE

# HOW MANY LEVELS EXIST AFTER EACH POSITION

hierarchy=["CEO","DIRECTOR","MANAGER","EMPLOYEE"]
def count_levels(data):
    if len(data)==0:
        return 0
    else:
        return 1+count_levels(data[1:])
result =count_levels (hierarchy)

print("result =",result)

#--------------------------------------------------------------------------------------------------------*****

# LAMBDA FUNCTION ---> a small function written in one line ,without giving it a normal function name

# it starts with lambda arguments : expression

lambda x :x*2
# lambda --> initialise the lambda function  where x  is input and x*2 final result

# calculate employee bonus
salary = 50000
calculate_bonus =lambda salary:salary*0.10
bonus=calculate_bonus(salary)
print("bonus =",bonus)

# calculate product,price after dicount
price=2000
discount=20
calculate_discounted_price = lambda price, discount: price - (price * .20)
print(calculate_discounted_price(price, discount))




# ********************************************************************************************************************
#

# EXCEPTION HANDLING ---> AN EXCEPTION IS AN ERROR THAT HAPPENS WHILE THE PROGRAM IS RUNNING

# TYPES OF ERRORS
#   1)  ZERO DIVISION ERROR ( INFINITY ) : --
sales =5000
customer=0
#  print(sales/customer) # zero division


#    2) value error
age="twenty"
#  print(int(age))

#    3) type error
salary=50000
bonus="50000"
#print(salary+bonus)   # invalid

#      4)  index error

employees=["John","Jane","Doe"]
# print(employees[3])  # index out of range

#      5) key error :

employee ={"name":"amit","salary":50000}
#print(employee["department"]) # key does not exists

#       6) name error :
age=40
# print(name) # variable name is not defined


# Exception handling is handle the above error so smooth execution of code

# try -except : ---->

# EXAMPLE :--
#customer order qty

qty="10"
try:
    qty=int(qty)
    print("order qty =",qty)
except ValueError:
    print("invalid order qty")


# find department

employee={"name":"riya","department":"sales","salary": 200000}
try:
    print("department =",employee["department"])
except KeyError:
    print("invalid department")


# multiple except blocks

# invalid employee coutn

employee="five"
units=500
try :
    employee=int(employee)
    result=units/employee
    print("result =",result)
except ValueError:
    print("employee count must be numeric")
except ZeroDivisionError:
    print("employee count cannot be zero")

# try -except -else

# try:
        # risky code
#   except:
        # handle exception
#   else:
        # code to run if no exception occurs

# customer payment

payment="2500"
try:
    payment=float(payment)
except ValueError:
    print("invalid payment")
else:
    print("payment =",payment)   # else and try block will execute together in this case


# try -except-finally

try:
    payment=float(payment)
except ValueError:
    print("invalid payment")
finally:
    print("finally")

# example
amount=10000
installments=0
try:
    payment=amount/installments
    print('installments =',payment)
except ZeroDivisionError:
    print("installments cannot be zero")
finally:
    print('payment calculation completed')


# try -except-else-finally:

try:
    payment=float(payment)
except ValueError:
    print("error code")
else:
    print("success code " )
finally:
    print("always run")

# invalid calculation

bill =1000
customer=5
try:
    amount=bill/customer
except ZeroDivisionError:
    print("customer cannot be zero  ")
else:
    print("amount per customer ",amount )
finally:
    print("invoice calculation finished ")

# raise keyword: ---> i know python thinks it technically okay , but according to the rule of business it is wrong
# syntax

# if condition:
#           raise ValueError('error message')

# example ---->
# withdrawl exceeding account balance

balance =10000
withdrawal =15000
try:
    balance=withdrawal/balanceg
except ZeroDivisionError:
    print("balance cannot be zero")
if withdrawal>balance:
    raise ValueError("withdrawal cannot be greater than balance")
balance=balance-withdrawal
# except ValueError as error:
#         print('transaction failed:',error)
# print("remaining    balance =",balance)