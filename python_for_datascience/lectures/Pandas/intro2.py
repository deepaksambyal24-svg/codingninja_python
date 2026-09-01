import pandas as pd
df=pd.read_csv('train_csv.csv')
print(df)

# mathematical operation  on series

# Q) ---> Add a fixed service fee

new_fare=df["Fare"].head(10)+10  # if we want to add 10 to each fare in the first 10 rows or not without using head

print(new_fare)

# apply 18 % increase in fare
fare_with_change=df["Fare"]*1.18
print(fare_with_change)

#-----------------------------------------------------------------------------------------------------------------