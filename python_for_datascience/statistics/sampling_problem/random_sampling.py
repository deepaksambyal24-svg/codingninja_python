import pandas as pd
import numpy as np
df=pd.read_csv('dataset.csv')
print(df.head())
sample=df.sample(n=500,random_state=1)
print(sample.head())
print(sample['income'].mean())
print(df['income'].mean())