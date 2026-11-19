from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
S=int(input())
E=int(input())
W=int(input())
for i in range(S,E+1,W):
    print(S,end=" ")
    cel=((S-32)*5/9)
    print(int(cel))

    i+=1
    S+=W
print()

























