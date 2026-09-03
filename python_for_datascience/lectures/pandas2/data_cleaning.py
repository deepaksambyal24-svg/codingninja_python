import pandas as pd
cust=pd.read_csv('customers.csv')
pro=pd.read_csv('products.csv')
pur=pd.read_csv('purchases.csv')
print(cust.head())
print(pro.head())
print(pur.head())


# identifying missing values

# isnull ()  and isna ()  ---> it shows whether the values in the dataframe are null or not


# count missing customer informatin

print(cust.isnull().sum())
print(cust.isnull().sum().sum())  # total number of missing values in the dataframe

# answer is true and false

print(cust['email'].isnull().any())  # True if there is any missing value in the email column
print(cust['email'].isna().any())  # True if there is any missing value in the email column

# dropping missing values



# remove missing values in email column

# dropna()  ---> it removes the missing values from the dataframe

email_null=cust.dropna(subset=['email'])   # shows the data and hide the null values in output

location_data=cust.dropna(subset=['state','postcode'])  # shows the data and hide the null values in output



# to remove null values from columns we can use dropna() method with axis=1
complete_column=cust.dropna(axis=1)  # removes the columns which have any missing values
print(complete_column)



# filling missing values
# fillna()  ---> it fills the missing values in the dataframe with a specified value
# ffill()  ---> it fills the missing values in the dataframe with the previous value
# mode()  ---> it fills the missing values in the dataframe with the most frequent value
#bfill()  ---> it fills the missing values in the dataframe with the next value

# replace missing values of email column with 'no email'
cust['email']=cust['email'].fillna('no email')
print(cust['email'])

print(cust['gender'].value_counts())
gender_mode=cust['gender'].mode()[0]
cust['gender']=(cust['gender'].fillna(gender_mode))
print(cust['gender'])

print(cust['gender'].value_counts())

cust['city']=cust['city'].ffill()
print(cust['city'])

cust['state']=cust['state'].ffill()
print(cust['state'])

# duplicate handling
# duplicated ()

# check exact duplicate customer rows
print(cust.duplicated(subset=['first_name']).sum())
print(cust.duplicated().sum())
