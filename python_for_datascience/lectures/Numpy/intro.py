# NUMPY has two sections numpy1 and numpy2


# numpy is numerical python , it works with large numerical data ,calculations become easy , statistical analysis
# it also works with other python libraries

# NUMPY Is also knows as NUMPY ARRAY list is heterohenous whereas arrays are hmogeneous (only numbers)

import numpy  as np
from numpy.ma.core import transpose
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

a = np.array([1,2,3,4,5])
print(type(a))


# analyse daily sales  of a store
a=np.array([12000,30000,150000,210000,250000])
print("avg sales = ",np.mean(a))
print("meddian sales = ",np.median(a))
print('std dev=',np.std(a))

# understand arrays
sales=np.array([10,9,99,71,90])
print(sales[0])


# numpy array /ndarray ( n-dimensional)
# 1d ---1 dimension   [10,20,30]
# 2d --- 2 dimension   [[10,20,30],[30,40,50]]
#3d---3 dimension       [


# product prices
prices =np.array([499,799,999,1499,1999])
print(prices[2])
# two stores and 3 products
# sales_2d=np.array([50,100,40],[60,120,55])
# print(sales_2d)


# create 3d array
sales=np.array([[[50,100,40],[60,120,55],[70,130,60]]])
print(sales)

arr = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
]

# dtype ---> what kind of value each numpy element store
a=np.array([10,20,30,40,50],dtype=float)
print(a)



# ensure product ratings are decimals

ratings =np.array([4,5,3,2,1,5,4],dtype=float)
print(ratings)

# numpy array attirbutes---> it describes about a particular object

# 1) ndim-----> how many dimensions does an array have ?

sales =np.array([10,20,30,40,50])
print(sales.ndim)
print(sales.shape)

# shape ----. how is the array arranged ?
sales=np.array([[10,20,30],[40,50,60]])
print(sales.ndim)
print(sales.shape)

# size ---> how many values are there all together
print(sales.size)

# itemsize --> how much memory does each element occupied
print(sales.itemsize) # retrun 8 for 2 byte for each element eg 12


# data ---gives access to memory buffer

# indexing and slicing :

sales =np.array([[10,20,30],[40,50,60],[70,80,90]])     # 2d array
print(sales[1,2])


# 3 d array ---> matrix,jrow ,column


sales=np.array([[[100,120,80],[130,150,90]],[[110,125,85],[140,160,95]]])

# to get month 2 store2 product 3
print(sales[1,0,2])
print(sales[0,1,1])



# boolean indexing /masking

sales=np.array([100,200,300,400,500])
# 100-keep,200-dont,300-keep,400-dont,500-keep

mask=np.array([True,False,True,True,True])
print(sales[mask])              # it will hide the value of index where value is true


# select high value orders (>100)
orders =np.array([1200,800,2500,500,3000])
mask=orders>1000
print(mask)
highest=orders[mask]
print(highest)


# employee eligible for bonus
scores=np.array([65,82,91,74,88,59])
mask=scores>=80
eligible=scores[mask]
print(mask)
print(f'these employees are elgible: {eligible}')

# slicing in arrays ;
# array[start:stop:step]
sales=np.array([100,120,130,125,150,170,180])
first_five=sales[:5]
print(first_five)

sales=np.array([100,120,130,125,150])
alternate=sales[::2]
print(alternate)


# two dimensional slicing

sales=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]])
print(sales[1:3,1:3])  # to get 60,70,100,110 1:3 for rows and 1: 3 is for columns 




# arthemetic operations with numpy : + - * / ?? ** %

a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(a+b)
print(abs(a-b))
print(a*b)
print(a//b)
print(a**3)



# transpose ()

c=transpose(a)
print(c)

# change store wise sales into month wise sales
sales =np.array([120,150,180])
sales1=np.array([[120,150,180],
                [90,110,130],
                [90,110,130]
                ])

print(sales1.T)          # CHANGE THE ROW INTO COLUMN AND COLUMN INTO ROW


# AXIS ---> it has only two 0,1 0 means column , 1 means rows
a=np.array([
    [10,20,30],
    [40,50,60]
    ])

print(np.sum(a,axis=0) )  # sum columns
print(np.sum(a,axis=1) )    # sum row


# SORTING ---> arranging values in either ascending or descending

# there are three are types or sorting asc is default ,np.sort () 2) arr.sort () 3) np.argssort ()

# np.sort()  ---> it gives us sorted copy and create a copy of the array

sales3=np.array([120,150,180])
sorted=np.sort(sales3)
print(sorted)
print(id(sales3))
print(id(sorted))

sales4=np.array([[500,300,700],
                [900,400,600],
               [ 350,800,450]
                ])
result=np.sort(sales4,axis=1)
result1=np.sort(sales4,axis=0)
print(sales4)
print(result)
print(result1)

# arr.sort() ---> inplace sort  it sort the original array it do not create other copy

sales5=np.array([500,100,700,300])
sales5.sort()
print(sales5)


sales6=np.array([[500,300,700],[900,400,600],[350,800,450]])
sales6.sort(axis=0)
print(sales6)

# np.argssort(0 ---> arg sort ask for where did these values came from, so it give the index of array insorted form
sales7 =np.array([500,300,700,900])
print(np.argsort(sales7))

# to sorted in desc order

sales9=np.array([40,10,50,20,30])
des=np.sort(sales9)[::-1]               # sort desc order
print(des)


sales10=np.array([[500,300,700],
                 [900,400,600],
                 [350,800,450]])
res=np.sort(sales10,axis=1)[:,:-1]   # first colon is for entire 2d matrix
print(res)

# concatenating arrays ---> join arrays

jan=np.array([[100,200,300],
              [400,500,600],
              [350,800,450]])
feb=np.array([[100,200,300],
              [900,400,600],
              [350,800,450]])
res=np.concatenate((jan,feb),axis=0)
res1=np.concatenate((feb,jan),axis=1)
print(res1)
print(jan)
print(feb)
print(res)


# reshape ---> changing the data arrangement without changing the actual data

# eg-->  [1 2 3 4 5 6 7 8 9 10]   linear 1x10
# to reshape this   in 2x5 or 5x2 columns

sales11=np.array([100,200,300,220,240,490,320,590,560,980,760,245])
print(sales11.shape)


res=sales11.reshape(2,6)


## reshape (-1)

# arange  --> generate a sequence of numbers for a particular limit

# convert 28 element into weekly format
sales12=np.arange(1,29)
weekly_sales=sales12.reshape(7,4)
print(weekly_sales)

# reshape -1 flatten the array it convert 2d array into 1 d array

shape13=np.array([[100,120,140],[200,220,240]])
f=shape13.reshape(-1)
print(f)


# splitting arrays :----> split ()  divide use to break an array into two or more arrays

sales14=np.array([100,120,150,160,190,200,220,240,260])
print(sales14.shape)
sub=np.split(sales14,3)
for s in sub:
    print(s)

# split employees into teams

employees =np.array([1,2,3,4,5,6,7,8,9])
team=np.split(employees,3)
for member in team:
    print(member)


data=np.array([[100,10,5],[200,20,8],[150,15,6]])
cols=np.split(data,3,axis=1)
sal=cols[0]
profit=cols[1]
revenue=cols[2]
print('sales:')
print(sal)
print('profit:')
print(profit)
print('revenue:')
print(revenue)


# STASTICAL FUNCTIONS IN NUMPY ------> MAX ,MIN,MEAN, AVG ,MODE,MEDIAN ,SUM,STD


# mean()---> use to get the average of an array
sales14=np.array([1200,1500,1100,1800,1400])
avg=sales14.mean(axis=0)
print(avg)

sales_15=np.array([[1200,1500,1100,1800],
                   [1300,1800,1900,1799],
                   [2000,5000,4500,70000]])
p=np.mean(sales_15,axis=0)
print(p)



# median(0 ---> middle value after sorting the data

sales_16=np.array([1200,1500,1100,1800,8900])
print(np.median(sales_16))

sales_17=np.array([[1200,1500,1100,1800],
                   [1400,5600,6700,1400],
                   [4500,1400,1500,1700]])
p1=np.median(sales_17,axis=0)
print(p1)

# standard deviation ---> how spread out the value are form the mean

sales_18=np.array([1200,1500,1100,1800])
sales_19=np.array([50,160,40,180,70])
print(np.std(sales_18))
print(np.std(sales_19))


# min and max

print(np.min(sales_18))
print(np.max(sales_18,axis=0))

# sum ()  ---> total of arrays 1d  or 2d arrays

print(np.sum(sales_18,axis=0))

# broadcasting ---> when we apply same operation individualy for each element of the array

# salary of employee and give bonus 10 % bonus on salary

salary=np.array([30000,50000,77000,90000,100000])
new_salary=salary*1.10
print(new_salary)


# zeros () ---> intialize the array with zero values

zero_array=np.zeros((10,5))   # also intializewith data type ie dtype function
print(zero_array)


# ones (0 ----> intialize matrix with 1
ones_array=np.ones((10,5))
print(ones_array)

# full() ---> create an array and fill every value with the value i have given

full_array=np.full(10,100)   # note it hase single bracket
print(full_array)

full_array1=np.full((4,3),20)       # 2d array
print(full_array1)


# eye() ----> identity like matrix so it fill diagnaly all element in a matrix with 1 and rest will be 0

eye_array=np.eye(4)
print(eye_array)    # create a matrix of 4x4 with 1 diagnoly filled and rest are zero


# arange() ---> start stop , and step

arange_array=np.arange(1,10,2)  # create a list of odd numbers
print(arange_array)


# random() ---> generate random numbers from 0 to 1
random_array=np.random.randint(1,10,2)
random_array1=np.random.random(4)
print(random_array1)
print(random_array)

# linspace() -----> equal spaces between random number so we decide the gap between the number s

lins_array=np.linspace(0,10,5)  # equally spaced random values  from 0 to 10
print(lins_array)

print(np.linspace(1,20,8))

