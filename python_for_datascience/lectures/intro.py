import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

from function import return_keyword

#
# df = pd.read_csv("dataset/cars.csv")
# print(df.head())      # First 5 rows
# print(df.tail())      # Last 5 rows
# print(df.shape)       # Rows and columns
# print(df.columns)     # Column names
# print(df.info())      # Data types
# print(df.describe())  # Numerical summary
# sep parameter it is separator what you placed between multiple values inside the print statement

print("data",'science','Apple','banana',sep='-')
# input function
#take input from user it allows the program to pause and wait till the user and wait for user input
a= input("enter your name:") # by default it takes string as input
print('hello' ,a)
# '+' is used for concat two strings
fruit=input("enter your fruit name:")
color=input("enter your color:")
print('the'+ fruit ,'is',color)
# indentation - giving space before a line of code, in other programming languages represented by {}
x=3
y=5
if x>3:
    print('more')
# variables are the containers used to store date
print(id(x))  # it store the reference of  object
'''variable used for storing data manipulating data reusability readablity '''
# declare and assign the variable : creating the object and then assign the value
'''rules - only contain letter numbers and underscore () it cannot start with numbers and are 
case sensitive', and keywords not used, variable name cannot have space and special char 
between them'''
# reassignment of variables also known as UNPACKING
a,b,c=10,'deepak',100
# assign a value to multiple variable
x=y=z=50


# IDENTIFIERS : any name we use in python ie funtion name , class name variable all are identifiers
# keywords are not identifiers
'''
DATA TYPE :- number int float complex 
STRING DATA :- string 
LIST DATA :- list 
BOOLEAN DATA :- boolean  True and False
'''

# escape CHARACTERS
# 1. BACKSLASH \ After the backslash it is the part of text only
# eg print ('it's the toy")
# slash t : \t  tab character it add a tab space
print("name:\t",a)

#

