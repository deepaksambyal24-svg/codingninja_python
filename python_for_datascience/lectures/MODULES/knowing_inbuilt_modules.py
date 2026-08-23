# INBUILG MODULES


#    1) PLATFORM MODULE ---> It stores information such as OPERATING SYSTEM ,MACHINE ARCHITECTURE
#       ,PYTHON VERSION, IMPLEMENTATION

# it gives a basic report showing the system's environment


import platform
print(platform.python_version())
print(platform.system())
print(platform.release())
print(platform.platform())
print(platform.python_implementation())
print(platform.architecture())
print(platform.machine())
print(platform.IOSVersionInfo)

#  DATE TIME MODULE : -->
# datetime>now() --current date and time
# strftime(0 --> converts a date into a formatted text
# strptime() ---> converts formatted text to date
# timedelta() --> for duration of time
# from datetime import datetime,timedelta
# # an invoice is payable 30 days after 18th august 2026
#
# invoice_date=datetime.strptime("2026-08-18","%Y-%m-%d")
#
# due_date=invoice_date+timedelta(days=30)
# print(due_date.strftime('%d/%B/%Y'))

# MATH MODULE :

import math
#    math.sqrt(x)----> square root
# math.ceil(x) ---> round upward   eg--4.1---> 5
# math.floor(x) ----> round downward         eg 4.9 ---> 4
# math.factorial(x) --- calculate factorial
# math.pi---> value of pi
# math.log(x0 ---> logarithm



# EXAMPLES --- DELIVERY BOXES
products=100
cap_per_box=10
boxes_required=math.ceil(products/cap_per_box)
print(f'boxes_required:{boxes_required}')


# RANDOM MODULE ------> this module is used to generate a random number
import random

# funtion of random module
# random.random()----->      float from 0.0 till 1.0
# random.randint(a,b)---> integer from a to b including both
# random.choice(items) ---> one item
# random.choices(items,k=3) ---> k means repetitions with multiple choices
# random.sample(items,3) ---> unique choices duplicate not allowed
# random.shuffle(items) ---> changes list order

# PROMOTIONAL PRIZE DRAW
customer=['aarav','riya','kabir','meera','rohan']
random.seed(42)    # it is mandatory and also treated as syntax
winner=random.choice(customer)          # pich randomly one item from this list
print(f'winner is :{winner}')


# select unique audit orders
orders=['ord-101','ord-102','ord-103','ord-104','ord-105']
random.seed(42)
selected_order=random.sample(orders,3)
print(f'selected_order:{selected_order}')



# OS MODULE :--> Operating system module  computer contain folders path , paths and os of the machine
# It connects like a bridge between the components of the machine to the python program

import os
print(os.getcwd()) # which folder you are working now
print(os.listdir())  # show every thing in the folder


import random
# seed (42) when we need to see the same random numbers generated for different purpose


# AB TESTING through random module

customers = ['C-101','C-102','C-103','C-104','C-105']


group_a=customers[:3]
group_b=customers[3:]
print('design_a,',group_a)
print('design_b,',group_b)



print(random.random())
print(random.randint(1,100))
print(random.choice(['aarav','riya','kabir','meera','rohan']))
