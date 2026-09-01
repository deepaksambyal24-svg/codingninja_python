import pandas as pd
df=pd.read_csv('train_csv.csv')
print(df)

# dataframe ---> complete data set

# creating a dataframe which include some of the columns from the original dataset
customer_df=df[['PassengerId','Name','Survived','Age']]   # we can reorder the columns as per our requirement
customer_df=customer_df[['PassengerId','Name','Age','Survived']].head(10)  # not selecting entire data set but only first 10 rows


print(customer_df)


# create a manual dataframe
# HR  creating a dataframe from 5 emloyees
emplyees =[{'id':101,'name':'Aman','salary':500000,'department':'IT'},
           {'id':102,'name':'Sneha','salary':600000,'department':'HR'},
           {'id':103,'name':'Rahul','salary':700000,'department':'Finance'},
           {'id':104,'name':'Priya','salary':800000,'department':'Marketing'},
           {'id':105,'name':'Vikram','salary':900000,'department':'IT'}]
manual_df=pd.DataFrame(emplyees)
print(manual_df)


# how to create an empty dataframe and then add data to it

empty_data=pd.DataFrame()

print(empty_data)

# accessing dataframe columns and rows

#1) how to access single column from dataframe
# 2) multiple columns from dataframe
# 3) access rows from dataframe using loc and iloc
# 4) access entire rows from dataframe


# 1 access the single column from dataframe

df['Name']  # this will return a series
print(df['Name'])

multiple_column=df[['Name','Survived']].head(10)
print(multiple_column)

# how to access single row

print(df.loc[3])
print(df.iloc[3,4])  # this will return the value of 4th row and 5th column


# boolean indexing

 # whereever the condition is true it will show me True and wherever the condition is false it will show me False

    # this will return a series of True and False values
print(df['Sex']=='female')

female_passenger=df[df['Sex']=='female']  # this will return the rows where the condition is True
print(female_passenger.shape)


# our of entire data how many rows we have age greater than 40
higher_age=df[df['Age']>40]
print(higher_age.shape)

# look for no of people who are female and pcall 3
target_passengers=df[(df['Sex']=='female') & (df['Pclass']==3)]
print(target_passengers.shape)
# if you want the data not shpe
print(target_passengers)

print(target_passengers[['PassengerId','Sex' ,'Pclass']].head(10))


# how to do slicing of dataframe

# select rows 2-4 and for specifc columns
print(df.loc[2:4,['PassengerId','Name','Age']])

# rows with index 1-3 and first 3 columns
print(df.iloc[1:4,0:3])  # this will return the rows with index 1-3 and first 3 columns


