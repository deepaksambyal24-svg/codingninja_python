# probability distribution


# random variable --A variable that can take on different numercial values each associated with some values of probablilty
# there are two kind of variable
# if head comes , you win 1 dollar , if tail comes , you lose 1  X outcome of the expt and Y reward of the coin toss and is cal
# is called random variable
# value of Y it takes are 1, -1 so probabability 0.5 0.5
# Y is the discrete random variable because can take value finite number of values ,
# COUNTABLY INFINITE ---> they can be countable



# example 2 ---->
# rolling two dice
# y REPRESENTS THE SUM OF  THE NUMBERS APPEARING WHEN TWO DICE ARE ROLLED
# (1,1) ,(1,2) , ( 1,3) , (1,5 ) AND (1,6)
 # Y CAN TAKE 2,3,4,5,6,7,,8,9,10,11,12  TTL OF 11 VALUES


# example 3
# Z represents the outcome of a dice roll
# z={ 1,2,3,4,5,6}
# rule is IF YOUR ROLL A 1,2,3 = WIN 2 DOLLARS
# IF ROL A 4,5,6 YOU WIN 5 DOLLARS
# Y CAN TAKE TWO VALUES ON LY 2 , 45

# SO the probability distribution of W IS 2,5
# FOR 2 IT IS 1/2 = .5     AND FOR 5   ___. .5

# PROBABILITY DISTRIBUTION IT  DESCRIBE PROBABILITY ARE DISTRIBUTED OVER THE  VALUES OF THE RANDOM VARIABLE
#  IF THE RANDOM VARIABLE IS DISCRETE THE PROBALITY DISTIBUTON IS A TABLE
# IF THE RANDOM VARIABLE IS CONTINUOUS ,IT WOULD MOST LIKELY BE CURVE

# Example  3 red balls and 2 blue balls
# random x ---> represents the number of red balls drawn when two balls are drawn without replacements
# two balls are drasn without replcaement

# 1st case --> ist ball blue , 2nd ball is also blue( x=0 )
# 2 case ---> ist ball red , 2nd balll is red  x =1
# 3rd case  ---> ist ball red , 2nd ball is blue x=1
# 4th case ---> ist ball red , 2nd ball red x=2


# x can take up : 0,1,2
# these  are dependent events
# x canp(x=0 ) = 2/5 * 1/4 = 1/10

# probablity (

#   WHAT ARE THE CONTINUOUS RANDOM VARIABLES
# It cant take any any values  ini a given range
# eg the hieght of people
# there is no finite values so probability of a continous variable  taking a specific value is zero
#     X( represents teh height of students in a class )

# P(X=165.8) =0  BECAUSE 1/ INFINITY IS ZERO
# In this case focus is probability of a random variable falling within a range of value
# ex probalibility of x falling between 162 and 164 cm


# Histogram : T he  range of variable is divided into intervals ( bins ) and height represents the height counted
# and ploted


# generating  a 1000 random height  from a normal distribution
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
np.random.seed(0)
height =np.random.normal(loc=170,scale=10,size=1000)
# the normal distribution has two parameter mean std
# mean =170(  and std dev = 10  , and size =1000
print(height)
# normal distributaion is also called as gaussian distribution
# a probability distibution in which most values are centered around mean and fewer values occurs
# as we go away from the mean in either direction
# a bell shaped curved
# four characterstics are
# shape is symmetrical
# the mean is equal to mean = mode
# most of teh values are near the mean
# THE AREA UNDER THE CURVE IS ALWAYS EQUAL TO ONE
plt.hist(height, bins=15 , edgecolor='black',)

plt.title('Histogram of height')
plt.xlabel('height')
plt.ylabel('number of people')
plt.axvline(x=170, color='red')
plt.show()



# approximatley 3.86 is the width of each bin



# REVERSE THING
from scipy.stats import norm
mu,std=norm.fit(height)
# find mu and std sigma so that the data follows a vell curve
 # it is called the estimation of parameter
plt.hist(height,bins =10,density =True, alpha =0.6 ,color='g',edgecolor='black')
         # plot the PDF
         # fetching max and min values on x
xmin,xmax=plt.xlim()
x=np.linspace(xmin,xmax,100)
# p represent the probablity p.pdf it is probability density
p=norm.pdf(x,mu,std)
plt.plot(x,p,'k',linewidth=2)
plt.show()
# it is probability density curve for height /probability distibution of heights

# the area under the curve is the value of y
# P9X=150 =0 , Curve density of  x = 150 =.004 and P(X=160) =0 prob density for x =160 =.020
# area under to point s is  ie x to be lying 150 and 160 cm will be equal # to area under the curve
