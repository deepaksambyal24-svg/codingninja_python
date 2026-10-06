import pandas as pd
import numpy as np
import scipy.stats as stats
np.random.seed(0)
num_samples=1000
discrete_data=np.random.randint(1,10,size=num_samples)
print(discrete_data)
df_discrete=pd.DataFrame(discrete_data,columns=['Number_of_children'])
print(df_discrete.head())
print(df_discrete.shape)
print(df_discrete)


# caluclate the mode using scipoi
mode_discrete=stats.mode(df_discrete['Number_of_children'])
print(mode_discrete)
mean_discrete=df_discrete['Number_of_children'].mean()

print(mean_discrete)

# so in descrete data mode is best value for imputation


# generate a continuous  data
continuous_data=np.random.rand(num_samples)*10
df_continuous=pd.DataFrame(continuous_data,columns=['Number_of_children'])
print(df_continuous.head())
mean_continuous=df_continuous['Number_of_children'].mean()
print(mean_continuous)
mode_continuous=stats.mode(df_continuous['Number_of_children'])
print(mode_continuous)

# for continuous data , mode is not meaningful at all because the values too varied to repeat

# generate cardinal data ---->
colors=['red','blue','green','orange']
nominal_data=np.random.choice(colors,num_samples )
df_nominal=pd.DataFrame(nominal_data,columns=['colors'])
print(df_nominal.head())

# how to generate the ordinal data
satisfaction_level=['low','medium','high']
oridinal_data=np.random.choice(satisfaction_level,num_samples ,p=[0.3,0.4,0.3])  # probability of low mediam , high


