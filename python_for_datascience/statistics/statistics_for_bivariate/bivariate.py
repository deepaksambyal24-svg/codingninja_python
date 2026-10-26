import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# FLOW CHART FOR CHOOSING THE RIGHT STATISTICAL TEST
# 1) IDENTIFY THE TYPES OF VARIABLES
# CONTINUOUS ( GOT TO STEP 2 ) , CATEGORICAL ( GO TO STEP 4)
# 2) HOW MANY NUMBERS OF GROUPS BEING COMPARED
# WE COMPARING SAMPLE MEAN TO POPULATION MEAN :  ONE SAMPLE TEST OR Z TEST
# TWO GROUPS : --> GO TO STEP 3
# MORE THAN TWO GROUPS : --- ANOVA
# 3) RELATIONSHIP BETWEEN THE TWO GROUPS
        # INDEPENDENT GROUPS : USE AN INDIPENDENT TWO SAMPLE TEST
        # PAIRED GROUP : PAIRED SAMPLE T TEST

# 4) TESTING ASSOCIATION BETWEEN TWO CATEGORICAL VARIABLE : CHI SQUARE ( KI SQUARE ) TEST OF INDEPENDENCE

df=pd.read_csv('flight_delays_train.csv')
print(df.T)
print(df.describe())
print(df.shape)

 # hypotheisis test is : ---> is there a difference in flight distance for delayed vs non delayes flights
 # we have two group delayed yes and delayed no so there are two independent test

 # null hypothesis (CHANGE) H0 : ----> the average flight distance is same for both groups
 # H1 :--> THE AVERAGE FLIGHT DISTANCE DIFFERS SIGNIFICANTLY BETWEEN DELAYED AND NON DELAYED
delayed_flight=df[df['dep_delayed_15min']=='Y']
non_delayed_flight=df[df['dep_delayed_15min']=='N']
print(delayed_flight)
print(delayed_flight.shape)
print(non_delayed_flight.shape)
from scipy.stats import ttest_ind
t_stat,p_value=ttest_ind(delayed_flight['Distance'].dropna(),non_delayed_flight['Distance'].dropna())
print(t_stat,p_value)
# p_value ( 0.38) > (0.05) greater than alpha
# so we fail to reject the null hypothesis
# there is no significant difference in flight distance between delayed flight and non deleyed flight


#######################################################################################################################


# CHI SQUARE TEST OR CHI SQUARE OF INDEPENDENCE------>
'''Is there a significant association between age group and product preference  '''

# is there a significant association between two categorical variable age group and product preference
# we compare observed frequencies in each category to the frequencies that would be expected if there were no association
# between the variables.
# H0:---> there is no association between age group and product preference
# H1:---> There is no association between age group and product preference

# KEY PROPERTIES : -->
# IT IS USED WITH CATEGORICAL DATA AND IT IS A RIGHT SKEWED DISTIBUTION
# IT IS ALWAYS NON NEGATIVE
# DEGREE OF FREEDOM = (R-1)*(C-1)  , WHERE r and c are number of rows and column s
import numpy as np
import scipy.stats as stats
observed=np.array([[50,30,20],[30,40,30],[20,30,50]])
print(observed)
chi2_stat,dof,p_value,expected=stats.chi2_contingency(observed)
print(chi2_stat)
# expected ---> these are frequencies if there was no association between the variable s
# chi square stat: how much the expected frequencies or observed frequencies deviate from the expected frequencies
# if there is no association between the variables under the null hypothesis
# p_value> 0.05
# fail to reject the null hypotheissi
# there is no significant association between the age group and product preferences

# exercise 2::::---> whether the days of the week are related to likelihood of the delays
# h0 : there is no association between the day of the week and likelihood of delay
# h1 : there is a association between the day of the week and likelihood of delay

# creating a contigency table of the counts of delays by day of the week
contingency_table=pd.crosstab(df['DayOfWeek'],df['dep_delayed_15min'])
print(contingency_table)
chi2_stat,p_value,df,expected=stats.chi2_contingency(contingency_table)
print(p_value)

# it is again greater the aplha ie p_value   > 0.05
# fail to reject the null hypotheisis



# how to perform dependent t test

