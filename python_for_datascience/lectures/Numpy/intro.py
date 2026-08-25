# NUMPY has two sections numpy1 and numpy2


# numpy is numerical python , it works with large numerical data ,calculations become easy , statistical analysis
# it also works with other python libraries

# NUMPY Is also knows as NUMPY ARRAY list is heterohenous whereas arrays are hmogeneous (only numbers)

import numpy  as np
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






