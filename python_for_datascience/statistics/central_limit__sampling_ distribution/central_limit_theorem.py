import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# CENTRAL LIMIT THEOREM

df=pd.read_excel('fraud_data.xlsx')
print(df.T)
print(df.shape)
popluation_mean=df['amt'].mean()
print(f'population mean is : {popluation_mean}')
sample=df['amt'].sample(n=1000,random_state=42)
print(f'sample mean is :{sample}')
sample_mean=sample.mean()
print(sample_mean)

# impact of sample size on sample mean
sample_sizes = [10,50,100,1000,5000]

sample_means = [df["amt"].sample(n = size,random_state = 42).mean() for size in sample_sizes]
print(f'sample mean is : {sample_means}')

# for zipping together
for size ,mean in zip(sample_sizes,sample_means):
    print(f'{size} is : {mean}')

# as the sample size increase , the sample mean is a better estimation of the population mean


# SAMPLING DISTRIBUTION
# SAMPLE MEAN ----> mean of single sample
# SAMPLING DISTRIBUTION MEAN :---> IT is mean of all all possible sample mean which approximate the pop. mean
# sampling distribtution

# central limit theorem ---> the distribution of sample mean will tend to be normal regardless of the original
# distribution of the data as long as the sample size is sufficiently large

def visualize_clt(data,sample_size,num_samples):
    sample_mean=[np.mean(np.random.choice(data,size=sample_size))for _ in range(num_samples)]
    plt.hist(sample_mean,bins=30,edgecolor='black',alpha=0.7)





# calculate the mean of the sample means ( sampling distribution mean )
# and also calles as sampling distribution
# sample_means_distribution =[np.mean(np.random.choice(df['amount'],size=100))] for _ in range(1000)]


# a lot of statistical methods assume that the data is normally distributed
#
# standard error ;----> sigma / square root of n
# = population std. dev /sqrt(n)
#
# SE= sample std deviation (s) / sqrt(n)
# std dev : -- measures the spread of individual data points around the po mean

# standard error : --- it measures the spread of sample mean around the pop mean
