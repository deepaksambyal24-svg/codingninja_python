import pandas as pd
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


