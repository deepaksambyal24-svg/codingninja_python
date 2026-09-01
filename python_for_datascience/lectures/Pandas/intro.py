# pandas ---> is used  for data cleaning , data manipulation
import pandas as pd
from numpy.ma.core import size

df=pd.read_csv('train_csv.csv')
print(df)

# pandas ---> it is library used to work with data  it similar like excel in python
# storing data , read csv and excel ,select rows and columns and filter data ,calculate  totals and averages ,
# clean missing values , analyze business data .

# structures of pandas :
# series ---> column in dataset
# dataframe ---> complete data set

# SERIES ---> one particular column




employee_name = pd.Series(
    ['aman', 'sneha', 'rohit', 'mohit', 'tanvi', 'karishma', 'rahul'],
    index=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th']
)

print(employee_name)

# print(df.shape)
# print(df.columns)
# print(df.shape)
details=df[["Name","Age","Fare"]]
print(details.head(4))


# I WANT TO STORE

# SET INDEX FUNCTION --> set_index ()
# store the fares with passenger ids , if we want to assign calues of one series as an index

fare_by_passenger=df.set_index("PassengerId")["Fare"]
print(fare_by_passenger.head(10))



#creating series
# 1) scalar values --->
# create default booking status using scalar
status=pd.Series("Pending",index=df["PassengerId"].head(4))
print(status)

# 2 ) create a series from lists   and 4 will be its default value
fare_list=df["Fare"].head().tolist()
fare_series=pd.Series(fare_list)
print(fare_series)

# 3) from dictionary

passenger_clas={892:3,893:3,894:2}

class_series=pd.Series(passenger_clas)

# accessing series : indexing and slicing
#Loc----access the element from series using their labels
# iloc ---access elements from a series using their index


# loc
# find  the name of passenger whose id is 892
names=df.set_index('PassengerId')["Name"]
print(names.loc[892])

# find fares for three passengers ----> 892,893,894
fare=df.set_index('PassengerId')["Fare"]
print(fare.loc[[892,893,894]])

# take position 1 to 3 from age

age =df["Age"]
print(age.iloc[1:4])


# series atttributes --> name ,dtype ,shape ,size,index

# sant the shape of survived series
import numpy as np
# check the overall properties of the fare column
fare=df["Fare"]
print("name:",fare.name)
print('datatype:',fare.dtype)
print("shape",fare.shape)
print("size",size)
print("dimension",fare.ndim)
print("missing values :",fare.hasnans)    # check missing values funciotn in numpy
print("no of missing value",fare.isnull().sum())
print("check uniqueness:",fare.is_unique)   # check unique vlaues


# series methods , head (0 ,tail(0 ,describe() , value_counts() ,sort_values() ,sort_index() ,drop()
# replace() ,isnull() ,notnull()


age_summary=df["Age"].describe()
print(age_summary)



# value_count ---> works like group by count function
embarked_count=df["Embarked"].value_counts()
print(embarked_count)

# checking the missing values

missing_age = df["Age"].isnull().sum()
print(missing_age)
available_age=df["Age"].notnull().sum()
print(available_age)


# sort values
sorted_asc_age=df.sort_values(by="Age")
sorted_age=df.sort_values(by=["Age"],ascending=False)
print(sorted_age)
print(sorted_asc_age)

df.sort_index()   # default desc order

# drop function  to drop or remove the column

df.drop(index=3)
df.drop(columns=["Age"])

df.drop(columns=["Embarked","PassengerId","Sex"])
df.drop(index=[4,5])
# it remove date only in console not from sourse or excel book


# replace funciton

df["Embarked"].replace("Q","Queenstown")
# to remove multiple values
df["Embarked"].replace({"Q":"queenstown","S":"Southampton","C":"chesboug"})



