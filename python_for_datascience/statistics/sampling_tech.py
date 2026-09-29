import pandas as pd
import numpy as np
df_population=pd.read_csv('Population_Survey_Data.csv')
print(df_population.head().T)

# SAMPLE RANDOM DATA
random_sample=df_population.sample(n=100,random_state=1)
print(random_sample.head())
# random state =0 is similar to seed


# STRATIFIED SAMPLING

print(df_population['Region'])

stratified_sample=df_population.groupby('Region',group_keys=False).apply(lambda x:x.sample(min(len(x),25)))
print(stratified_sample.head())

# cluster sampling

df_manufacturing=pd.read_csv('Manufacturing_Data.csv')
print(df_manufacturing.head().T)
print(df_manufacturing.shape)

cluster_sampling=df_manufacturing['BatchNumber'].unique()
print(cluster_sampling)
selected_clusters=np.random.choice(cluster_sampling,5,replace=False)
# replace =True -->here cluster are differnect every time because has not selected seed ,
# selected if a no is selected once not selected again

print(selected_clusters)
cluster_sample=df_manufacturing[df_manufacturing['BatchNumber'].isin(selected_clusters)]
print(cluster_sample.head())
# rows


# SYSTEMATIC SAMPLING
systematic_sampling=df_population.iloc[::10,:]
print(systematic_sampling.head())

# calculate the acutal mean income
actual_mean_income=df_population['Income'].mean()
print(f' actual mean: {actual_mean_income}')

# calculate mean income form random sample
random_sample_mean_income=random_sample['Income'].mean()
print(random_sample_mean_income)


stratified_sample_mean_income=stratified_sample['Income'].mean()
print(stratified_sample_mean_income)

systematic_sample_mean_income=df_population['Income'].mean()
print(systematic_sample_mean_income)

# increasing random sample

random_sample_2=df_population.sample(n=200,random_state=2)
random_sample2_mean_income=random_sample_2['Income'].mean()
print(random_sample2_mean_income)