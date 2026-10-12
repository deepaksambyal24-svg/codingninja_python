import pandas as pd

# Write your code from here
df=pd.read_csv('train.csv')
filter= df[(df['Embarked']=='C') & (df['Sex']=='female')]
print(filter.shape)