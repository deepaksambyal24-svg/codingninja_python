import pandas as pd
import numpy as np


# slicing using index lebles
data=[10,20,30,40,50]
s=pd.Series(data,index=["a","b","c","d","e"])
slice_by_levesls=s['b':'d']
print(slice_by_levesls)


# creating serias by two lit value and keys
data=[10,20,30,40]
index=['india','usa','uk','France']
# creating the series
series=pd.Series(data,index=index)
print(series)

print(f'index:{series.index}')
print(f'values:{series.values}')

# return or set the name of the series

series.name='demo'
print('name:')
print(series.name)
print(series.shape)
# attributes
# check whether the series is empty or no t
print(series.empty)  # empty --. is empty string
print(series.hasnans)
print(series.isnull())
print(series.isnull().sum())
print(series.unique())
print(series.ndim)


# methods of series

marks=[86,90,92,89,78]
students=['alice','bob','charlie','david','eva']
student_series=pd.Series(marks,index=students)
print(student_series)

# print ----head
print(student_series.head(1))
print(student_series.tail(1))

# print describe
print(student_series.describe())


# value count __ return a series containing counts of unique values

print(student_series.value_counts())



# sort values
print(student_series.sort_index())

# drop a value
print(student_series.drop('charlie'))  # remove a series it does not change the actual series


# replace ()
print(student_series.replace(85,86))


# not null
#res=student_series.notnull.sum()


# dropping an element with inplece Without inplace:
# ○ The drop method returns a new Series.
# ○ The original Series remains unchanged.
# ● With inplace=True:
# ○ The drop method modifies the original Series directly.
# ○ No new Series is returned.
student_series.drop('charlie',inplace=True)
print(student_series)


# addition of two series

seriesA = pd.Series([1,2,3,4,5], index =['a', 'b', 'c', 'd', 'e'])
print('seriesA:')
print(seriesA)
seriesB = pd.Series([10,20,-10,-50,100],index = ['z', 'y', 'a',
'c', 'e'])
print('seriesB')
print(seriesB)

# Performing addition
result_addition = seriesA + seriesB
print("Addition of seriesA and seriesB:")
print(result_addition)

# fill na
result_addition_fillna=result_addition.fillna(0)
print(result_addition_fillna)

# drop na values

result_addition_drop=result_addition.dropna()
print(result_addition_drop)


# SUBTRACTION OF TWO SERIES
result_subtraction=seriesA-seriesB
print("Subtraction of seriesB from seriesA:")
print(result_subtraction)


# multiplication of series
esult_multiplication=seriesB*seriesA
print("Multiplication of seriesB from seriesA:")
print(esult_multiplication)


# DATA FRAME --> MULTIPLE COMLUMN

# creating a dataframe
empty_df=pd.DataFrame()
print(empty_df)
import numpy as np
import pandas as pd

data=np.array([[25,'New York'],
               [30,'Los Angeles'],
               [35,'Chicago'],
               [40,'Houston']
               ])
df=pd.DataFrame(data,columns=['Age','Name'])
print(df)

# creating a dataframe form a list of dictionaries
data = [
{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
{'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
{'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'},
{'Name': 'David', 'Age': 40, 'City': 'Houston'}
]
df = pd.DataFrame(data)
print(df)
Customers=pd.read_excel('customers.xlsx')
Products=pd.read_excel('products.xlsx')
Purchases=pd.read_excel('purchases.xlsx')
print(type(Customers))

# accessing a column
customer_names=Customers['first_name']
print(customer_names)
print(Customers.T)

# .loc --> column_data = DataFrame.loc[:, 'column_name']

first_column_loc=Customers.loc[:,'id']
print(first_column_loc)
first_column_iloc=Customers.iloc[:,0]
print(first_column_iloc)

# accessing multiple columns
columns_data=Customers[['id','first_name']]
print(columns_data)


# applying .loc on multiple column

customer_info_loc=Customers.loc[:,['first_name','city']]
print(customer_info_loc)

# applying iloc on multiple column

columns_data_iloc=Customers.iloc[:,[0,2]]
print(columns_data_iloc)

# accessing a single row using .loc

customer_row_loc=Customers.loc[2]
print(customer_row_loc)

# accessing ros using iloc
customer_row_iloc=Customers.iloc[2]
print(customer_row_loc)

# BOOLEAN INDEXING
# SYNTAX = DataFrame[boolean _conidion]
male_customers=Customers[Customers['gender']=='Male']
print(male_customers)

#filter products where the company is 'Dynazzy'
filtered_products = Products[Products['company'] == 'Dynazzy']
print("Filtered Products:")
print(filtered_products)


# include or and and condition
# Filter rows where first name is 'Tobit' or 'Natale'
filtered_customers = Customers[(Customers['first_name'] ==
'Tobit') | (Customers['first_name'] == 'Natale')]
filtered_customers


# slicing on dataframe element through slicing
# Slicing rows and columns using .loc
# Example: Slice rows 2 to 4 (inclusive) and columns 'product_num'
# and 'paid'
sliced_loc = Purchases.loc[2:4, ['product_num', 'paid']]
print("Using .loc for slicing:")
print(sliced_loc)

# Slicing rows and columns using .iloc
# Example: Slice rows 1 to 4 (exclusive) and columns 1 to 3
# (exclusive)
sliced_iloc = Purchase.iloc[1:4, 1:3]
print("\nUsing .iloc for slicing:")
print(sliced_iloc)

