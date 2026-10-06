import pandas as pd
from sklearn.gaussian_process.kernels import Product

customers=pd.read_csv('customers.csv')
print(customers  )
products=pd.read_csv('products.csv')
print(products)
purchases=pd.read_csv('purchases.csv')
print(purchases)


# dataframe attributes --->size ,empty ,ndim
# index , columns , shape , size , dtypes , values , head() , tail() , info() , describe()

print(purchases.shape)

# index ---> it shows the row labels of the dataframe
print(customers.index)  # start =1 stop =1000 and step =1

# shape ---> it shows the number of rows and columns in the dataframe
print(customers.shape)  # (1000, 4) 1000 rows and 4 columns

# columns ---> it shows the column labels of the dataframe
print(customers.columns)  # Index(['customer_id', 'first_name', 'last_name', 'email'], dtype='object')

# dtypes ---> it shows the data types of each column in the dataframe
print(customers.dtypes)  # customer_id     int64
                         # first_name     object
                         # last_name      object
                         # email          object

# values ---> it shows the values of the dataframe in the form of a numpy array
print(customers.values)  # [[1 'John' 'Doe' 'john.doe@example.com']]

# size ---> it shows the total number of elements in the dataframe
print(customers.size)  #row x columns =11000

# empty ---> it shows whether the dataframe is empty or not
print(customers.empty)  # False or True if the dataframe is empty

# ndim ---> it shows the number of dimensions of the dataframe
print(customers.ndim)  # 2 row and columns is called as 2 dimensions


# dataframe inspection methods ---> head() , tail() , info() , describe() transpose()


print(customers.head())  # shows the first 5 rows of the dataframe
print(customers.tail())  # shows the last 5 rows of the dataframe
print(customers.info())  # shows information about the dataframe how many
# rows and columns are there and how many non-null values are there in each
# column and memonry usage of the dataframe
print(customers.describe())  # shows statistical information about the dataframe
print(customers.T)  # shows the transpose of the dataframe
print(customers.transpose())


# concatenation
customers['full_name'] = customers['first_name'] + ' ' + customers['last_name']
print(customers[['full_name']])


# adding the rows ie adding new customers to the existing dataframe
new_customers={'id':1001,'first_name':'Aman','last_name':'Kumar','email':'aman.kumar@example.com','gender':'Male',
               'street':'Aman Kumar','streetname':'Aman Kumar','city':'Aman Kumar','state':'Aman Kumar','country':'Aman Kumar','zipcode':'Aman Kumar'}
customers.loc[len(customers)] = new_customers
customers.loc[1002]=new_customers


 # deleting and renaming rows /column s:
 # remove unwanted columns from the dataframe

#customers.drop(columns=['Unnamed: 0'], inplace=True)   # inplace means that the
# changes will be made to the original dataframe and not a copy of it
#products.drop(columns="Unnamed: 0", inplace=True)\
print(products.head(10))


# Rename cost column to unit_cost
products.rename(columns={"cost": "unit_cost"}, inplace=True)
print(products.head(10))


###################################################################################################################


# UNIQUE VALUES AND NUNIQUE VALUES
# unique values  ---> it shows the unique names from the column
# nunique (0 ---> gives the number of unique values form the column


# unique ()
print(customers['gender'].unique() ) # it shows the unique names from the column

# count the gender categories

print(customers['gender'].nunique())

print(customers.columns)

print(customers['city'].nunique())


# concantenation : stacking dataframes by rows (axis=0) or columns (axis=1) just like union join in sql

print(purchases.shape)
first_half=purchases.iloc[:3000]
second_half=purchases.iloc[3000:]
print(first_half)
print(second_half)

# join both first_half and second_hald as stack

all_purchases=pd.concat([first_half,second_half],axis=0)
print(all_purchases )  # (6000, 4) 6000 rows and 4 columns


# divide the customers dataframe into two halves  for basic info and address info

basic_info=[['customer_id','first_name','last_name','email','gender']]
address_info=[['customer_id','street','streetname','city','state','country','zipcode']]
print(basic_info)
print(address_info)

# customers_report=pd.concat([basic_info,address_info],axis=1)
#
# print(customers_report)


# MERGE  AND JOIN


# MERGE ---> combining tables through common columns or indices just like join in sql


# purchase id ,customerid,name

customer_purchase=pd.merge(purchases,customers[['id','first_name']],
                           left_on='customer_num',right_on='id',how="left",suffixes=('_purchases','_customers'))
print(customer_purchase)  # left join ---> all the rows from the left table and matching rows from the right table
# right join ---> all the rows from the right table and matching rows from the left table
# inner join ---> only the matching rows from both tables
# outer join ---> all the rows from both tables and matching rows from both tables
#





