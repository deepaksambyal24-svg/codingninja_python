# STANDARD ERROR :- IT measure how much the sMPLE MEAN DIFFER FROM A SINGEL SAMPLE WROULD DIFFER FORM THE TRUE POPULATION MEAN
 # is its is less mean is a good approximation for the true pop mean
 # if my se is more that mean sample mean is not a good approximatin for he treu pop
 # whenever sample size is less se is m ore , and sample mean not a good approximation for a pop mean

 # FOR THIS WE NEED T_ TEST  It is used the sample size is small we dont use the normal distribution we use t distribution


 ########################################################################
 # T TEST:-- >

 # DEGREES OF FREEDOM : -----> It is number of independent values in a calculation that are free to vary is called
 # as degree of freedom
 # df = n-1 where n is sample size for n=50 df =49 , 80 df-=79
 # eg ---> there are three students with heights of 150 , 160 , 170 cm .
 # if we know avg, and two heights we can determine the third height
 # only two values can freely vary
 # so x3 is automatically fixed

 # z = (sample - mean - pop mean )/ se zscore or z statistic , se = pop man / sart(n)

 # t = (sample mean - pop mean ) /se , here se = samplemean / sqrt

# there are two types of t test
# 1 sample T-TEST : ---- > campare the sample mean to a hypothetical population mean
# eg -- > testing whether the average height of a group of students is significantly different form the natinal average height

# a company claims that the avg daily sales are 200000 . a sample of 12 days is taken and the average daily sales
# observed 210,00 with std dev of 15, 000 . test the company's claim at 5 % significance level

import scipy.stats as stats
import matplotlib.pyplot as plt
sample_mean=210000
population_mean=200000
sample_std_dev=15000
sample_size=12
se=sample_mean/sample_size**.5
t_statistic=sample_mean-population_mean/se
print(t_statistic)

df=sample_size-1
# calculate the p _ value
p_value=2*stats.t.sf(abs(t_statistic),df)
print(p_value)
if p_value> .5:
    print ('we fail to reject the null hypothesis')
else:
    print ('we pass the null hypothesis')

    # result is we fail to reject the null hypothesis , the data provides a strong evidence in favour of the company claim


# INDEPENDENT two sample t test ------> group 1 , group 2 we compare their sampmle means , we compare the sample mean of
# two group to see if there is any evidence that the associated population are significantly  different
# eg ---> we comparing the test scores of students from two different school .

# DEPENDENT or paired T - TEST ---> In this case we compare the mean two related group .eg - same group of individuals
# before and after a treatment
# test scores but then gave a training program ,then comparing test scores before and after the program


# ANOVA( ANALYSIS OF VARIANCE)  TEST : --> A COMPANY HAS THREE DRINKS A , B, C . IS THERE SIGNIFICANT DIFFERENCE IN THE AVERAGE CAFFEINE CONTENT
# AMONGST THESE THREE TYPES OF DRINK
# DRINK A : --- 5 CANS  _ CAFFIENE CONTENT= [ 105,110,98,107,103]
# DRINK B : ---5 CANS [ 130,125,132,128,129]
# DRINK C : --5 CANS  [ 120,115,117,119 ,121]
# QUESNTION; IS THE AVG CAFFEINE CONTENT SIGNIFICANTLY DIFFERENT ACOROSS THESE THREE TYPES OF DRINKS
# ANOVA TEST ALLOWS US TO COMPARE THE MEAN OF THREE OR MORE GROUP AT ONCE TO SEE IF THEY ARE SIGNIFICANTLY DIFFERENT
# ARE ALL THE GROUP ARE SIMILAR
# TO DO THIS F _STATISTICS

# 1 ) CALCULATE THE MEAN OF EACH EACH GROUP : DETERMINE THE AVG CAFFEINE CONTENT FOR EACH TTYPES DRINK
# 2 ) CALCULATE THE OVERALL MEAN CAFFINE CONTENT ACROSS ALL THE THREE GROUP S
# 3) CALULATE WITHIN GROUP VARIATION , HOW MUCH INDIVIDUAL VALUES WITHIN EACH GROUPS DIFFER FROM THERE RESPTIVE
# SAMPLE MEANS /GROUP MEANS
# 4) BETWEEN GROUP VARIANCE : ---> CALCULATE HOW MUCH EACH OF THE GROUP MEAN VARY FROM THE OVERALL MEAN
# CALCULATE THE F - STATISTICS ----> VARIATIN BETWEEN GROUPS / VARIATION WITHIN GROUPS
# COMPARE THE F-STATISTIC TO A CRITICAL VALUE TO DETERMINE WHETHER THE OBSERVED DIFFERENCES ARE SIGNIFICANT
group_A=[ 105,110,98,107,103]
group_B=[ 130,125,132,128,129]
group_C=[ 120,115,117,119 ,121]
import numpy as np

# perform one way anova
f_statistics,p_value=stats.f_oneway(group_A,group_B,group_C)
print(f_statistics)
# p_value =0.68 > alpha (.05 )
# so we fail to reject the null hypotheisis
# there is no significant difference between the average caffeine content of drinks a , b, c