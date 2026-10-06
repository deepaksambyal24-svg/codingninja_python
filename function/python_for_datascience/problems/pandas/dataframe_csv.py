import pandas as pd

# Write your code from here
train=pd.read_csv("train.csv")
print(train.shape)
uni=train['Embarked']
print(uni.value_counts())