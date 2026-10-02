import pandas as pd
import numpy as np
df=pd.read_csv('cluster_data.csv')
print(df.head())
# Divide data into groups → randomly select some groups → take data from the selected groups.
clus=df['product'].unique()
print(clus)
cluster_sample=np.random.choice(clus,5,replace=False)
print(cluster_sample)
sample = df[df['product'].isin(cluster_sample)].groupby('product').sample(n=50, random_state=42)
sample_stats = sample.groupby('product')['price'].agg(
    ['mean', 'median']
)

print(sample_stats)
print(sample)