import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import  scipy.stats as stats
import seaborn as sns


# probability ---> branch of mathematics that deals with the likelihood or chance of getting different outcomes
# experiment ---> a process that leads to the occurrence of one and only one of several possible observations
# or it is a process or activity that leads to one of the many possible outcomes eg tossing a coin
# sample space ---> the set of all possible outcomes of an experiment is called sample space
# event ---> it denoted by (E) It is subset of sample space an event occurs when the outcomes
# of the experiment is a member of sample space
# eg tossing a coin sample space is {H, T} and event E = {H} or E = {T}
# example a six sided die sample space is {1, 2, 3, 4, 5, 6} and event E = {2, 4, 6} or E = {1, 3, 5} even or odd numbers
# and prime number P(E) := No. of the outcomes in the event E / No. of outcomes in the sample space S



# Types of Events in probability :--->
# INDEPENDENT EVENT :---> Two events A and B are independent if the occurence of A does not affect the occurence of B
# experiment : rolling a dice , flipping a coin
# EVNT : Rolling a 3 E(A) , getting a head E(B)
# p(a) =1/6 , p(b) = 1/2

# P( both events occureing ) = P(A) * P(B) = P(1/12)

# DEPENDENT EVENTS --> Occurence of one event impact the occurence of the other
# experiment is drawing two cards  without replace ment

# A; probability of drawing an ace P(A) -- 4 /52
# B probablity of drawing a king given  an ace is drawn first P(B) ---P(B|A) = 4/51
# p( both veent occuring togetther ) : P(A) * P(B|A) = 4/52 * 4/51

# MUTUALLY EXCLUSIVE EVENTS : A AND B ARE M.E if the are not occur at the same time
# experiment : rolling a dice
# A --- Getting a 3 --- P(A) = 1/6
# B --- Getting a 5 --- P(B) = 1/6

# P(BOTH EVENT OCCURING  = p(a) + p (b)

# simulating the event using
import random

# independent event

# simulation for rolling a dice and flipping a coin
die_rolls=[random.randint(1,6) for _ in range(10000)]

# simulating the coin flip

coin_flip=[random.choice(['H','T'])  for _ in range(10000)]
print(len(coin_flip))
print(len(die_rolls))

# count the occurence of rolling a  3  and flipping a head togther

# combine two list together
zipped_list=zip(die_rolls,coin_flip)
print(zipped_list)

# we are want to coint how many times 3 and h are occuring together
both_events = sum(1 for die,coin in zip(die_rolls,coin_flip) if die==3 and coin=='H')
print(both_events)
print(f'probability of both occuring {both_events/100000}')  # empeirical probability
# therotical probabiltiy = 0.0834

# as the experiment is repeated  a large number of times atleast a 1000 in that case emperical probability to theoretical probabiltiy


# FOR MUTUALLY EXCLUSIVE EVENTS

dice_rolls=[random.randint(1,6) for _ in range(100000)]
print(dice_rolls)
# count occurences rolling of 3 or rolling of 5
either_event=sum(1 for roll in die_rolls if roll==3 or roll== 5 )
print(either_event)

p_either_5_or_3=either_event/10000
print(p_either_5_or_3)
print(f'theortically {2/6}')