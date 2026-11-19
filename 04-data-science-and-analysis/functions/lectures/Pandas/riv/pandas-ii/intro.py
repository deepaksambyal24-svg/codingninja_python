import pandas as pd



products = pd.read_excel('products.xlsx')
purchases = pd.read_excel('purchases.xlsx')
customers = pd.read_excel('customers.xlsx')
print(customers.index )


# shape function

print(customers.shape)

# columns function
print(customers.columns)

# dtype : return data type of each column
print(customers.dtypes)

print(customers['state'].dtypes)



print(customers.values)

# size returns the number of element in Dataframe
print(customers.size)    # return rox x columnn


# empty  return true or false

print(customers.empty)

# ndim
print(customers.ndim)

print(customers.info())
print(customers.describe())

#m transpose

print(customers.transpose())


# create a new column with a scalar value
# it add a new column in dataframe and assign usa to all rows
customers['Country']='USA'
print(customers)

# adding a column from a list
membership_status=['gold','silver','gold','bronze','silver']*200
customers['membership_status']=membership_status
print(customers)

# adding a column based on another column
customers['full_name']=customers['first_name']+customers['last_name']
print(customers)


# adding a new row to data frame
#
# customers.loc['1000'] = [1001,'Romain', 'Westrip',
# 'bwestrip52@symantec.com', 'Male', 90.0, None,None, None,
# 'Georgia', 83732.0, 'USA', 'Romain Westrip']
# print(customers.tail())

# deleting rows or oclumn form a dataframe

# customers.drop(index='1000',inplace=True)
# print(customers)

# delete column form a list
# columns_to_drop=['country','full_name']
# customers.drop(columns=columns_to_drop,inplace=True)


# renaming the first row to 'firstcustomer'
customers.rename(index={0:'FirstCustomers'})        # row with index number 0 should be renamed to firstcustomer

print(customers)
# create a dictionary mapping old index labels to new index labels

rename_dict={0:'FirstCustomers',
             2:'SecondCustomers',
             3:'ThirdCustomers',  }
print(customers.rename(index=rename_dict))


# renaming column labels of a dataframe
customers.rename(columns={
'street_num': 'street_number',
'street_name': 'street_address'
})
print(customers.T )



# finding the unique values

unique_genders=customers['gender'].unique()
print(unique_genders)

# nunique method

#counting the number of unique values in the gender column
count_unique_genders=customers['gender'].nunique()
print(count_unique_genders)

# type conversion of columns
# syntax :df['column_name'] = df['column_name'].astype(new_dtype)
# purchases['purch_date']=pd.to_datetime(purchases['purch_date'])---> give errror

#convert paid  column to numeric

print(purchases.T)

purchases['paid'] = purchases['paid'].str.replace('[\$,]', '',
regex=True).astype(float)
print(purchases.dtypes)
print(purchases['paid'] )
print(products['cost'])
products['cost']=products['cost'].replace('[\$,]','',regex=True).astype(float)
print(products.dtypes)
print(products['cost'] )
print(customers['postcode'])


# understanding joining merging and concatenation of dataframes

combined_df=pd.concat([customers,purchases,products],axis=0)
print(combined_df.T)
com_df=pd.concat([customers,purchases,products],axis=1)
print(com_df.T)

# merging  ---> combine on one or more keys when we need to comibine two datasets based on a common column or index

merged_df=pd.merge(customers,purchases,on='id',how='inner')

# display the merged dataframe
print(merged_df.T)


#  pd.merge(left, right, on='key_column', how='join_type',
# suffixes=('_left_suffix', '_right_suffix') prefixes and sukprefixes are used to rename othe columns

 #Create sample DataFrames with overlapping column names
Customers = pd.DataFrame({
'id': [1, 2, 3],
'first_name': ['Alice', 'Bob', 'Charlie'],
'product': ['Book', 'Pen', 'Notebook']
})
Purchase = pd.DataFrame({
'id': [2, 3, 4],
'product': ['Pen', 'Notebook', 'Pencil'],
'amount': [5, 10, 15]
})
# Merge DataFrames with suffixes for overlapping columns
merged_df = pd.merge(Customers, Purchase, on='id', how='inner',
suffixes=('_cust', '_pur'))
print("Merged DataFrame with Suffixes:\n", merged_df)

# performing join operation on 'id' column Joining:Joiningisaconvenientmethodforcombiningcolumnsfromtwopotentially
# differently-indexedDataFramesintoasingleresultDataFrame.Itusesindexestojoin
# DataFrames
joined_df=customers.set_index('id').join(purchases).set_index('id')
print("Joined DataFrame :\n", joined_df)      # join two tables on one side to other



# how to handle missing values


# to find the missing values
null_values =customers.isnull()
print(null_values)

null_val=customers.isna()
print(null_val)

# check for missing values in each column of customers
missing_in_columns=customers.isnull().any()
print(missing_in_columns)

# check if any element in the boolean dataframe
any_element_true=customers.isnull().any().any()
print(any_element_true)

# calculate the number of nan values in each atttirbute column of the customers dataframe
nan_counts_per_attribute=customers.isnull().sum()
print(nan_counts_per_attribute)

# calculate the number of nan values for each row in the dataframe
nan_counts_per_row=customers.isnull().sum(axis=1)
print(nan_counts_per_row)

# find the total number of nan values in whole dataset
total_nan=customers.isnull().sum().sum()
print(total_nan)

# replace unknown with pd.na in paid column
print(customers.T)
print(purchases.T)
print(products.columns)


# convert the str to numeric using to_numeric function and handling the eror using coerce function
# syntax : --> df['Paid'] = pd.to_numeric(df['Paid'], errors='coerce'

# dropoing rows with any missing values in the copy

customers_copy=customers.copy()
customers_dropped_rows=customers_copy.dropna()

print(customers_dropped_rows)

# drop columns with any missing values from the copy
customers_dropped_columns = customers_copy.dropna(axis=1)
print(customers_dropped_columns)


# estimating imputing missing values

# filleing missing values in email because canot filled with statistics
customers['email'].fillna('Unknown', inplace=True)
print(customers)

# calculate the mode of the gender column

mode_gender=customers['gender'].mode()[0]

# fill missing values in gender column with the mode

customers['gender'].fillna(mode_gender,inplace=True)
print(customers)
#
# # Fill missing values with forward fill (ffill)
# customers['street_num'].fillna(method='ffill', inplace=True)
# customers['street_name'].fillna(method='ffill', inplace=True)
# customers['street_suffix'].fillna(method='ffill', inplace=True)
# # Print or check the updated DataFrame
# print(customers)

# Fill missing values with backward fill (bfill)
customers['city'].bfill(inplace=True)
customers['state'].bfill(inplace=True)
customers['postcode'].bfill(inplace=True)
print(customers)
# Print or check the updated DataFrame


# fFilling using interpolate
# Fills NaNs using linear interpolation. Used for linear filling of missing values.
# df['column_name'].interpolate(method='linear', inplace=True)


#Remove duplicates based on the 'first_name' column
customers_unique = customers.drop_duplicates(subset='first_name')
# Display the DataFrame with duplicates removed based on'first_name'

print("Customers DataFrame with Duplicates Removed Based on'first_name':")
print(customers_unique)


# data aggregation
print(purchases.max(numeric_only=True))
print(purchases.aggregate('max', numeric_only=True))
print(products.aggregate(['max','min'],numeric_only=True))


# group by function

# group by customer_num and compute sum of amount and paid
aggregated_purchase =purchases.groupby('purch_date').agg({'amount':'sum','paid':'sum'})
print(aggregated_purchase)