# Write your code from here
import pandas as pd

df = pd.read_csv('train.csv')
print(df.isnull().sum().sum())

