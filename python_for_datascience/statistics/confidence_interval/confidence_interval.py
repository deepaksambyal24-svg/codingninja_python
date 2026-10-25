# CONFIDENCE INTERVAL : ----->If someone says 95 % confidencec interval
# it is range of values , derived from sample data ,that is likely to conatin the unknown value of a  population parameter
# when we say 95 % confidence interval , it means dif we werre to take 100 samples and compute confidence interval for each
# of the sample about 95 of those interval whould caontain the true population mean .
# scenarion :
# average weight of its packaged flour bags is 1.0 kg . take a sample of 40 package and find out that the average weight is .98 kg
# with a std dev .1 kg
# we have to construct a 95 % confidence interval for the rue mean weights of the flour packets


sample_mean=.98
n=40
std_dev=.1
confidence_level=0.95
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
standard_error =sample_mean*np.sqrt(n)
print(standard_error)
# z-score for 95 % confidence interval is 1.96
z_score=1.96
confidence_interval = (sample_mean-z_score*standard_error,sample_mean+z_score*standard_error)
print(confidence_interval)
# result the 95 % confidence interval for the true mean weight of the flour packet is approximately  between this confidence interval

# interpretation : we are 95 % confident that the true mean weight of all packages of flour lies between 094.kg and 1.015 kg

# impact of sample size on confidence interval
# when we take a larger sample size
# standard erro r is the measure of varability in the sample mean
# and standard error is inversly proportional to the sample size
# by increasing the sample size we are getting narror confidence interval
# the narrower confidence interval provides a more precise estimation of the population mean, which makes the
# estimaton of pop mean becomes more reliable and it is opposite when sample size is small and leading to wider estimation
# IF SAMPLE SIZE IS SMALL THE PRECISEN WOULD BE DECREASING , AND LESS PRECISE
# A WIDER CONFIDENCE INTERVAL LESS PRECISE , REDUCED  UNCERTAINTY



# ######################################################################################################################
# TYPE _ I , TYPE -II ERROR


# TYPE -I error ( False Positives)  a type I error occurs when we reject the null hypothesis but it is actually True
# in other words we conclude that there is a difference  when actually there is no differencce

# eg --- > whether a new drug is ore effective than the standard treatment if you incorrectly reject the null hypothesis
# and colclude that the new drug is more effective  when it actually is not # # you have made a type I error
# a person is healthy but shows positive


# TYPE -II ERROR ( FALSE NEGATIVE ) : when we fail to reject accept the null hypothesis it is actually false
# we are concluding that there is no difference when actually there is a difference
 # if we fail to reject the nul hypotheis and conclude that there is no difference between the new drug and standard treatment
 # when actually the new drug is more effective than the standard treatment

# RELATION TO CONFIDENCE INTERVALS : ---
# A type I error occurs when our intervals does not contain the population parameters leading us to incorrectly reject the
# null hypothesis

# balancing the error : --- >
#  by adjusting the alpha or our significance level  , an alpha of 0.05 we are accepting the 5 percent of making
# type I error
# so an alpha of 0.01  there is a 1 % chance of making a type I error ( incorrectly rejecting the null hypothesis)

# A LOWER ALPHA STRICTER THRESHOLD , AND HIGHER ALPHA MEANS WE ARE ALLOWING A MORE ERROR

# POWER OF A STATISTICAL TEST : ---- > IT IS PROBABILITY OF CORRECTLY REJECTING THE NULL HYPOTHESIS WHEN IT IS FALSE



# SCENARIO : WHETHER A NEW DRUG LOWERS BLOOD CAMPARE TO A PLACEBO

# H0 --- > THE DRUG HAS NO EFFECT ( MEAN REDUCTION IN BLOOD PRESSURE =0 )

#  H1 : ----> THE DRUG REDUCES BLOOD PRESSURE ( MEAN REDUCTION > 0 )
from scipy.stats import norm

# function to calculate tpower of the test
def calculate_power ( sample_size, effect_size ,std_deviation ,alpha=0.05):
    standard_error=std_deviation*np.sqrt(n)
    # critical value for a one tailed test
    z_critical=norm.ppf(1-alpha)
    z_effect=effect_size/standard_error
    power = 1-norm.cdf(z_critical-z_effect)
    return power
effect_size = 5 # true reduction in blood pressure
std_deviation = 10
alpha = 0.05
sample_size = [20,50,100,200,500]
# calculate and print the power
poer_1=calculate_power(sample_size,effect_size,std_deviation,alpha)

for n in sample_size:
    power=calculate_power(n,effect_size,std_deviation,alpha)
    print(f'sample size :{n},power :{power:.2f}')

# probabitly of rejecting the null hypothesis shen it is actually true is decreasing

# when the sample size increases , chances of makin ga type ii error is decreasing
# if power is higher the of type ii eroor is lesser 
