# hypothesis testing :--->
# STEPS IN HYPOTHESIS TESTING :
# 1 We step two hypothesis which are competeing each other the first one is null hypothesis
# is called NULL HYPOTHESIS  . it assumes that there is no significant differene between sample mean and population mean
# it suggests that the observed data is similar to what we would expect from the population
# it is represented H0 mean (sample) = mean (population )

# ALTERNATE HYPOTHESIS = H1 :  it is completely opoosite of null hypothesis .there is a significant difference between
# the sample mean and population mean .
# mathematically H1: mean( sample ) not equal to mean (pop)

# STEP 2 :
#TO DECIDE THE SIGNIFICANT DIFFERENCE WE SET UP A THRESHOLD
# It is setting a threshold or tolerence : the threshold helps us decide  to
# mean (sample) is within a threshold distance from the population mean , we would accept that the sample mean
# equals the population mean (). if the mean of the sample outside a threadshold distance form pop mean , we would accpet that sample mean is dirrerent from the p
# population mean ()
# STEP 3 :
# accepting or rejet the null hypothesis :
# we would accept the null hypothesis or we would be rejecting the null hypothesis

# scenario : a compay packages flour in bags which are labeled 1 kg . QC team wants to ensure that the average weight of the flour
# is approximately equal to 1 kg r not as clamed on the label .
# WE PERFORM THE NULL HYPOTHESIS OR ALTERNATE HYPOTHESIS
# null hypothesis : - the average weight of bag is equal to 1 kg mathematically
# mean ( sample ) = 1kg
# ALTERNATE HYPOTHESIS : - THE AVERAGE WEIGHT OF THE BAG IS NOT EQUAL TO LABELED WEIGHT OR MEAN SAMPLE NOT EQUAL TO 1 KG
# POLULATION MEAN IS 1KG HERE
#

# SCENARIO :-A FACTORY THAT PRODUCES GADGETS AND THE MACHINE ARE SET TO PRODUCE AT A SPEED OF OF 50 UNITS PER HOUR .
#SO THE FACTORY MANGER WANTS TO VERFIY WHETHER THE SPEED IS ACTUALLY 50 UNITS PER HOUR .
# H0 : THE AVERAGE PRODUCTION SPEED IS QUAL TO 50 UNITS PER HOUR
# mean(sample)= 50 units per hour null hypothesis
# H1( ALTERNATE) : The avetrage speed is not 50 units per hour .
#mean9sample not equal to 50 units per hour



# EXAMPLE 3
# BASELINE SIGNUP RATE (BEFORE STARTING THE MARKETING COMPAIGN ) : 5 %
# THE NEW CAMPAIGN WOULD INCREASE THE SIGN UP RATE BY 20 %
# AVERAGE SIGN UP RATE HAS INCREAES BY 20 %  OR NOT , AVERAGE SINGUP RATE HAS BECOME 35 % OR NOT
# H0 :-- because the null hypothesis is hypothesiss that ooreesponds to no effect or no change
# H0 : The marketing campaign has no effect  , The meam(signup)= 5%
# H1 (ALTERNATE) : THE MARKETING COMPAIGN HAS SOME EFFECT  mean( signup) >  5%
# so this this case success for company is lies in if null hypothesis gets rejected



# THE ROLE OF NORMAL AND STANDARD NORMAL DISTRIBUTION IN HYPOTHESIS TESTING
# 1 NORMAL DISTRIBUTION : the sample mean will likely fall somewhere along the x a axis of samplig distribution . it
# the sample mean is close to pop mean , it will be near the centre of the curve  if the sample mean is far from the pop
# mean, it will be out towards the tails of the curve
# standard normal distribution : how far a data point is away from   mean in term of std deviation
# Z-SCORE = how far a std dev away a  datapoint  or a sample mean from the mean
# eg if ZSCORE =2  It means dta point is 2 std dev away from the mean
# zscore helps us to quantify the sample mean and pop mean
# sample mean : calculate the z-score correspoinding to the sample mean then compare it with a threshold


#   A common threshold is 1.96 SD .If the sample mean is within 1.96 SD'S from the mean , we consider it
# close enoght and we accept the null hypothesis
# 1.96 SD 's (tolerance level ) corresponds to a significance level /apha of 0.05
# we are allowing a  5% chance of making an error of rejecting the null hypothesis when it is actually true

# in simpler terms " i am okay with being wrong % % if the times when i say that sample mean is different from poulation mean"

# the sample mean is 1.3 sd away from the popultion mean
# 1.3 sd < 1.96 sd so we not rejecting null hypotheseis
# corresponding to 1. 3 sd P VALUE IS PROBABILTIY
# P VALUES IS THE PROBABILITY OF GETTING SAMPLE MEAN 1.3 SD FROM THE POP MEAN IF NULL HYPOTHESIS WAS TRUE , P VALUE 0.1
# P-VALUE > ALPHA ---> WE FAIL TO REJECT THE NULL HYPOTHESISS
# P-VALUE < APLHA WE REJECT THE NULL HYPOTHESIS


# SCENARIO : -- A factory produces light bulbs that are supposed to last an average of 800 hours , we take a sample of
# 50 light bulbs and find out that the actual lifespan is 790 hours . the standard error (SE0 for the sample is 7.5 hours
# # the population mean = 800 hours
# sample mean = 790 hours
# standard error : 7.5 hours
# significance level (alpha) : 0.05 ( which corresponds to 1.96 SD )
# h0  IS THE MEAN OF SAMPLE 790 = mean(pop : 800)
# h1: mean(sample: 790) is stasticaly different mean( pop : 800 )
## corresponding to a sample mean , there has to be a z -score
# z= (sample mean -pop.mean) / se = (790-800)/7.5 = -1.33
#calulate the p values
from scipy.stats import norm
z=-1.33
p_value=2*norm.cdf(z)
print(p_value)
# p value (8.18 ) > alpha (0.5) so we accept the hypothesis

# stepts 

