
number = int(input())

# Check if exactly one of the two conditions is true
cond1 = number > 100
cond2 = number % 7 == 0
# Output: True if exactly one condition is true, otherwise False
# Use logical operators to determine if exactly one condition is true


print((cond1 or cond2) and not (cond1 and cond2))   # XOR OPERATION 


