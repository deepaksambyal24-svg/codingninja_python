# Given set1 & set2
set1 = {2, 3, 4, 7, 8}
set2 = {3, 5, 6, 7, 9}

# Write your code here
a=set1^set2
print(f"Symmetric Difference: {a}")
b=a.issubset(set1)
print(f"Is symmetric difference a subset of set1: {b}")