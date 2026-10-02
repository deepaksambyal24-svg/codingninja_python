import pandas as pd
import numpy as np
df=pd.read_csv('dataset.csv')
print(df.head())
# binning the data into 5 bins
df['age_bin']=pd.cut(df['age'],bins=[18,30,45,60,80],labels=['18-30','31-45','46-60','61-80'])
print(df.head())
print(df['age_bin'].value_counts())
sample_from_bin=df.groupby('age_bin',observed=True).sample(n=200,random_state=0)
sample_mean = sample_from_bin.groupby('age_bin')['income'].mean()
print(sample_mean)
print(df['income'].mean())