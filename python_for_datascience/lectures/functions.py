#FUNCTIONS ---> Without function repeated code , if the formula change we must change it everywhere, more opportunities to make mistakes
# a function a blovk of code created to perform a particular task
# function used for automation , avoid repeatation , reduce errors make programs easier to understand
# and to moke code easy to modify , dividing a large application into smaller units

# def is used to create functions

# TYPES OF FUNCTION -->
# BUILT IN FUNCTIONS --> print(), sum() ,mean() , float() , int(0 , list ()
#USER DEFINED FUNCTIONS ----> create by user

# syntax for userdefined function ---> def name of the function (parameter)
#                                               syntax



# APPLY 10 % DISCOUNT ON ALL ORDERS ABOVE 5000


def company_discount(amount):
    if amount > 5000:
        return amount*.90
    return amount
print(company_discount(8000))


# employees  selling more than one 100000 receives 10 incentives other wire

def incentive(sale):
    if sale >100000:
        return sale*0.10
    else:
        return 0
print(incentive(120000))



# PARAMETERS AND ARGUMENTS ---> Parameter are the placeholder pass inside a function  and d
# arguments are the value we have passed when calling a function


# greet any employee of your choice with a customised message


def welcome(name):
    return print('welcome ',name, "greeting of the day!!")

welcome("david")


# calculate revenue

def revenue(price,quantity):
    return price*quantity

print(revenue(100,5))

# POSITIONAL ARGUMENTS --->
def employee(name,department):
    print(name,"department is ",department)
employee("david",1)

# employee informatin


def emp(name,role):
    print(name,"-",role)
emp("deepak",'data analyst')

# ARBITRARY ARGUMENTS ---> if we dont know how many argument we would use inside our function

# it will take extra space for extra parameters and does not throw an error

def total_sales(*sales):
   return sum(sales)
total_sales(100,5)







# calculate the average of all the ratings
def calculate_rating(*ratings):
    return sum(ratings)/len(ratings)
print(calculate_rating(15,7,7,8,9,10))

# KWARGS --- keywords arguments : instead of mentioning the position of parameters , we mention parameters names


def emp(name,department):
    print(name,"-",department)
emp(department="data analyst",name="deepak")

# customer registration :
def customer(name,age,city):
    print(name,"-",age,"-",city)
customer(city="deepak",age=30,name="david")  # even we have changed the position of the
# parameters , it will not throw an error because we have used keywords arguments


# customer details

def cust(**details):
    print(details)
cust(name="deepak",age=30,city="delhi")  # it will take extra space for extra parameters
# and does not throw an error


# PRODUCT INFORMATION


def product_info(**details):
    print(details)
product_info(product_name="iphone",model=20001,price=10000)


# DEFAULT ARGUMENTS

def calculate_bill(amount,deliveru_fee=50):
    return amount*deliveru_fee
calculate_bill(amount=100) # it does not require to pass the delivery fee
# because we have already set a default value for it

# IMPORTANT RULE ---> NON DEFAULT PARAMETERS MUST COME BEFORE DEFALUT PARAMETERS


# restaurant bill will charge a fixed gst
def bill_cal(amount,tax=.18):
    return amount+amount*tax
print(bill_cal(amount=100,tax=.18))


# passing different data types into functions

def total_sales (sales):
    return sum(sales)
monthly_sale=[100,200,300,400,500]
print(total_sales(monthly_sale))


# dictionary

def show_info(product):
    print(product['name'])
    print(product['price'])
show_info({'name':'laptop','price':1000})


# RETURN () ---->  It is a way to exit a function and send a value back to whoever executed the function
# if no explicit return exit , it return None

def profit(revenue,cost):
    return revenue-cost
print(profit(1000,500))

# print vs return


# return means return the value to the caller and print means display the value on the screen

def profit () :
    print(30000)


profit()



# RETURNING----> return multiple values

def  sales_summary(sales) :
    total=sum(sales)
    highest=max(sales)
    return total,highest
sales_summary([2000,45000,10000,900000])

# show the net salary and the tax amount from the salary
def  salary_summary(salary) :
    tax=salary*.10
    paid_salary=salary-tax
    return paid_salary,tax
print(salary_summary(2000))

# passing a fucntion as an argument:
# def processs (function,data)
#           return function(data)

# apply a discount strategy :
def regular_discount(price):
    return price*0.95
def premium_dicount(price):
    return price*0.90
def calculate_price(discount_function,price):
    return discount_function(price)
calculate_price(premium_dicount,1000)

# pass a function to show the final salary after adding the bonus

def bonus(salary):
    return .10*salary

def cal_salary(bonus_func, salary):
    return salary + bonus_func(salary)

print(cal_salary(bonus,10000))


#------------------------------------------------------------------------------------------------------------#


# SCOPE ------> SCOPES ARE OF TWO TYPES     GLOBAL AND LOCAL SCOPE

# LOACAL VARIABLES ---> variables created inside a function are called
# local variables and can only be accessed inside the function


# GLOBAL VARIABLE --> variables created outside a function are
# called global variables and can be accessed anywhere in the program


# global scope /variable
# company tax rate
tax_rate=0.18
def calculate_tax(amount):
    return amount*tax_rate
calculate_tax(400000)

# GLOBAL VARIABLE
# show the name of the country
country="india"
def locaion():
    print(country)


locaion()


# local variable

def profit():
    revenue=500000
    cost=300000
    profit=revenue-cost
    print(profit)
profit()


# calculate revenue using qty and price to show both the scope of variable


price=100  # global


def calculte_price():
    quantity=10          # local
    ttl_price=price*quantity
    print(ttl_price)
calculte_price()



# update values of global variable :

# def function-name():
#      global variable_name
#   variable_name=new_value


target=10000000
def update_target():
    global target
    target=1500000

print(update_target())


# change the session mode of a classroom from offline to online


mode="offline"

def change_mode():
    global mode
    mode="online"

change_mode()
print(mode)



# NAME SPACES ---> where does python keep track of names and their objects

# there are three types of namespace

# 1)  BUILT IN ----> print,len,sum,max,min

# print(len(10,20,30) len is a built in function which is used to find the length of an object

# profit=1000 so both are called as name space


# 2) GLOBAL
# 3) LOCAL


# LEGB RULE ---> LOCAL ----> ENCLOSING-------> GLOBAL ------> BUILT IN  (FINDING RULES)


# LOCAL ----
x=10
def test():
    x=200
    print(x)
test()


# E ----> ENCLOSING  ie function inside another function


def outer():
    x=200
    def inner():
        print(x)

outer()


# G ---> global

x=300
def outer():
    def inner():
        print(x)
    inner()


# B---
def test():
    print(len[1,2,3,4,5])

company_tax=0.18                        # 3) global function
def finance_department():
    department_tax=0.12             # 2) enclosed fucntion
    def tax_cal(amount):
        special_tax=0.05                # 1)  locaal inner most
        print(special_tax)
        print(department_tax)
        print(company_tax)
        print(len([1,2,3,4,5]))             #  4) built in
    tax_cal(10000)
finance_department()


#  VARIABLE SHADOW ---> variable shadow means the closer variable
#  temporarily hides variable with same name
# Variable shadowing means a variable in an inner scope uses the same name as
# a variable from an outer scope, temporarily hiding the outer variable.

'''The purpose of shadowing isn't to change the outer variable; it lets an 
inner scope use the same name for a different value without affecting the outer variable.
For example, a function can safely use x for its own work while the outside x remains unchanged.'''


x=10
def out():
    x=20
    def inner():
        x=40
        print(x)
    inner()

# multiple nested function

def sales_calculator(price,qty):
    def revenue():
        return price*qty
    def tax():
        return revenue()*.18
    return revenue(), tax()

sales_calculator(100, 10)