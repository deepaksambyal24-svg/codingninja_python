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
