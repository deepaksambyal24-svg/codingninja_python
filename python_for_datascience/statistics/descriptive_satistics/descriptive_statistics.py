# descriptive statistics;--->
# range = maximum value - minimum value
# 56,64,92,85,73
# range = 92 - 36 = 56 so very simple and quick measure to calculate the variation in the data set.
# it is sensitive to outliers and does not provide information about the distribution of the data.
# a single very low and very high value can significantly affect the range
# , making it less reliable for datasets with outliers.

# IQR --->
"""It stands for interquartile range, which is a measure of statistical dispersion
that describes the range within which the central 50% of the data falls.
It is calculated as the difference between the third quartile (Q3)
and the first quartile (Q1) of a dataset. The IQR is less affected by
outliers and provides a better understanding of the spread of the data."""


# steps to calculate IQR:
# 1. Arrange the data in ascending order.
# 2. Find the median (Q2) of the dataset.
# 3. Divide the dataset into two halves: the lower half (below Q2)
#    and the upper half (above Q2).
# 4. Find the median of the lower half (Q1) and the median of the upper half (Q3).
# 5. Calculate the IQR using the formula: IQR = Q3 - Q1
# 6. The IQR represents the range within which
# data---> 48,56,63,564,71,78,82,85,89,92,99
# for odd median is middle point and for even median is average of two middle points
# median (even no of value ) = mean of n/a+n/2+1 = mean of 5th and 6th value = 71+78/2 = 74.5
# median means 50 % of data is below and 50% of data is above the median value
# also called as 2nd quartile (Q2)
# Q1 --. median of lower half = 56,63,64,71,78 = 64 MEDIAN OF THE IST HALF OF DATA
#Q3 --. median of upper half = 82,85,89,92,99 = 89 MEDIAN OF THE 2ND HALF OF DATA
# IQR = Q3 - Q1 = 89 - 64 = 25
# Q1 IS 25 % OF THE DATA IS LESS THAN 63
# Q3 IS 75 % OF THE DATA IS LESS THAN 89
# q4 is 100 % of the data is less than 99
# interpretation of IQR:
# middle 50 % of test score are within 22 points of each other,
# which indicates a moderate spread of the data.
# IQR is not affected by outliers, making it a more robust measure of variability compared to the range.
# can be ideal for dataset with outliers


# -------------------------------------------------------------------------------------------------------*
# VARIANCE --->
# a variance is a measure of how much the values in a data set differ from the mean or the average data set
# it provides the sense of overall spread in the data
# var(x) = (sum of (x - mean)^2)/n
# n= no of values in the data set
# mue = mean of the data set
import pandas as pd
import numpy as np
sale=np.array([100,150,200,130,170,160,180,190,170])
sale.sort()
print(sale)

#varianve of 400 means that there is a significant spread around the mean dailay sales ,
# suggesting a varibaility in the daily performance
# UNIT OF VARIANCE ---> SQUARE OF THE UNITS OF THE ORIGINAL DATA
# INTERPRETATION OF VARIANCE: it is an issue to interpret variance directly
# because it is in squared units, which can be less intuitive.
# A higher variance indicates greater variability in the data,
# while a lower variance suggests that the data points are closer to the mean.


# TO OVERCOME THIS ISSUE, WE USE STANDARD DEVIATION, WHICH IS THE SQUARE ROOT OF VARIANCE
# BASICALLY WE CANCELING THE SQUARE UNITS OF VARIANCE AND GETTING BACK TO THE ORIGINAL UNITS OF THE DATA
# STANDARD DEVIATION --->
# it is a measure of the amount of variation or dispersion in a set of values.
# A SD OF 20 MEANS THAT , ON AVERAGE DAILY SALES DEVIATE 20 DOLLARS FORM 160 DOLLARS
# BOTH GIVES THE VARIABLITY IN THE DATA


# SKEWNESS--->it measures the asymmetry in the data distribution

# positive skewness or right skew ---> there is tail of distribution on the right side of the mean
# negative skewness or left skew ---> there is tail of distribution on the left side of the mean
# skewness = 0 means the data is perfectly symmetrical
# we know mean is sensitive to outliers
# if the distribution is positively skewed, most people have income below the mean with the long
# tail on the right side where a small number of people having ve

#NEGATIVE SKEWNESS OR LEFT SKEW---> there is tail of distribution on the left side of the mean
# MOST people have income higher than the mean  with a long tail on the left side where a small
# number of people having very low income


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
# sci use to calulate skewness and kurtosis
np.random.seed(42)
# simulating aright skewed positve skewed distibution
income_distribution=np.random.gamma(shape=2.0,scale=1000.0,size=1000)
# plot the distribution
sns.histplot(income_distribution,bins=30,kde=True)
plt.title("Income Distribution (Right Skewed)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()
skew_value=skew(income_distribution)
print(income_distribution.shape)
print(skew_value) # posive for right skewed distribution and negative for left skewed distribution


# KURTOSIS ---> it measures the "tailedness" of the data distribution
# HOW HEAVY OR THE LIGHT THE TAILS ARE TOLD BY KURTOSIS
from scipy.stats import kurtosis
np.random.seed(42)
portfolio_returns=np.random.normal(loc=0,scale=1,size=1000)
print(portfolio_returns)
portfolio_return=np.append(portfolio_returns,np.random.normal(loc=0,scale=5,size=50))
print(portfolio_return)
sns.histplot(portfolio_return,bins=30,kde=True)
plt.show()
kurt_value=kurtosis(portfolio_return)
print(kurt_value)
# it give 13 it states as high kurtosis , leptokurtic distribution with heavy tails and a sharp peak
# low kurtosiss -- platykurtic distribution with light tails and a flat peak
# means more  evenly spread spread out portfoliio

