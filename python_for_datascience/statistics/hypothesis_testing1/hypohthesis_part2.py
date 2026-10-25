#STEPS TO FOLLOW HYPOTHESIS
# 1 )  state the null and alternate hypothesis
# 2) we have to choose significance level 9aplh)
# 3) collect data and calculate the z score
# 4) Determine the p-value  or critical vale
# 5) accept or reject the null hypothesis based on the p value



# scenario - a company package flour in bags labeled 1 kg the qc team wants to ensure that the average wieght of the flour in the bags is indeed 1 kg
# H0 ---> THE AVG WRIGHT OF THE BAG IS 1K G
# H1 ALT H --> THE AVG WIGHT OF BAGS TIS NOT EQUAL TO LABELED WIGHT MEAN

# TO TEST HYPOTHESIS TAKE A SAMPLE OF 40 PACKAGE AND FIND THE AVG WEIGHT IS 0.98 KG THE STD DEV OF THE SAMPLE IS .1KG
import numpy as np
population_mean= 1.0
sample_mean = 0.98
n= 40
std_dev =.1
# to calculate the z score
# standard error = std dev / sqrt(n) = .1/
standart_error=(std_dev/np.sqrt(n))
print(standart_error)


# calculate the z score
z_score=(sample_mean-population_mean )/standart_error
print(z_score)

# calculate the p value ( two tailed test )
from scipy.stats import norm
p_value=2*norm.cdf(z_score)
print(p_value)
# which is greater than alpha ie we fail to reject the null hypothesis
# CONCLUSION -- > The avg weight of the flour packets is not significantly different form 1.kg

#EXAMPLE 2 :----> A COMPANY RUN A/B TEST ON THEIR WEBSITE TO SEE IF A NEW DESIGNED VERSION B IMPROVES THE CONVERSION
# RATE CONVERSION RATE COMPARED TO THE OLD DESIGN VERSION A . FROM A SAMPLE OF 1000 VISITORS , ON VERSION A 120 MADE A
# ACTUALLY MADE A PURCHASE FROM A SAMPLE OF 1200 VISITORS ON VERSION B 156 MADE A PURCHASE .

conversion_rateA=120/1000
conversion_rateB=156/1200
print(f'conversion rate for sample A :{conversion_rateA}')
print(conversion_rateB)

# the task would be determine the whether the new design has significantly improve the conversion rate

# hypothesis :--->
# H0 ---> THE CONVERSION RATE FOR VERSION A IS EQUAL TO CONVERSION RATE FOR VERSION B
# H1 ---> CONVERSION RATE FOR VERSION B IS NOT EQUAL OR DIFFERENT TO EACH OTHER
p1=120/1000
p2=156/1200
n1=1000
n2=1200

# pooledproportion
p_pool=(120+156)/(1000+1200)

# standard error for the difference in proportions
se = np.sqrt(p_pool* (1-p_pool) * (1/n1 + 1/n2))
print(f'standard error is : {se}')

# z score for the difference in proportion

z_score=(p2-p1)/se
print(f'z_score is : {z_score}')


# p value
p_value=2*(1-norm.cdf(z_score))
print(f'p_value is : {p_value}')
if z_score> p_value:
    print('p_value is greater than p_value')
    print('we fail to reject the null hypothesis','there is no significant difference '
                                                  'in the conversion rates between the two website designs')
else:
    print('we accept to reject the null hypothesis')

# one tailed and two tailed test

# ONE TAILED TEST
# SCENARIO A SCHOOL CLAIMS THAT ITS NEW TEACHING METHOD INCREASES THE AVG TEST SCORE FROM 70 TO MORE THAN 70 .
# TAKE A SAMPLE OF 40 STUDENTS AND FIND THAT THEIR AVERAGE TEST SCORE IS 73 WITH THE STD DEV OF 8. THIS IS
# THE EXAMPLE OF ONE TAILED TEST
# INTEREST I HAVE IS WHETHER THE SAMPLE MEAN 73 IS SIGNIFICANTLY GREATER THAN  70 OR NOT
# ( ONE TAILED TEST )
# h0 ---> the average test scoe is less than or equal to 70
# H1 ---> THE AVERAGE TEST SCORE IS GREATER THAN 70

p_mean=70
s_mean=73
n1=40
std_d =8
se_it=std_d/np.sqrt(n1)
z_score_1=(s_mean-p_mean)/se_it
print(f'z_score is : {z_score_1}')
p_value= 1-norm.cdf(z_score_1)
print(f'p_value is : {p_value}')

if p_value< z_score_1:
    print('reject the null hypothesis')
    print(' conclusion : there is significant evidence to suggest that the new teaching method has increased test score ')
else:
    print( 'we accept the null hypothesis')

# when to use a one tailed test , when your are interest in testing whether a sample mean is significantly greater than
# or less than the hypothetical population mean

# when to use a two tailed test :--->
# when you are interested in testing whether a sample mean is significantly different form the population mean
# example when yu want to check whether a new drug has an effect on blood pressure  either increasing or decrease

# SCENARIO : ---> A RESEARCHER WANTS TO TEST WHETHER THE AVG WEIGHT OF A CERTAIN BRAND OF APPLES IS DIFFERENT FROM
# THE STD WEIGHT 150 GM
# A SAMPLE OF 30 APPLES IS TAKEN AND THE AVG WEIGHT  IS FOUND TO BE 145 GM  WITH A STD DEV OF 10 GM
# H0---> THE AVERAGE WIGHT OF APPLES IS 145 GM IS SAME AS 150 GM
# H1--> THE AVERAGE WEIGHT OF APPLES IS NOT EQUAL TO  145 GM

pop_mn=150
s_m=145
sd_2t=10
n=30
std_err=sd_2t/np.sqrt(n)
print(f'std_err is : {std_err}')

# calculate the z score
z_s=(s_m-pop_mn)/std_err
print(f'zscore  is : {z_s}')

# it is two tail test
p_v=2*norm.cdf(z_s)
print(f'p_value is : {p_v}')

# here p-value < alpha hence we reject the null hypothesis
# there is a significant evidence is suggest that the average wight of apples is different form 150 gm 