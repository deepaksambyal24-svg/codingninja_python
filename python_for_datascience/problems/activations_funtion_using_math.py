import math
# Don't make any changes to the above line



# Sigmoid Activation Function
def sigmoid(n):
    exp=math.exp(-n)
    return  1 / (1 + exp)



# ReLU Activation Function
def relu(n):
   return max(0,n)
# Tanh Activation Function
def tanh(n):
    return (math.exp(n)-math.exp(-n))/(math.exp(n)+math.exp(-n))