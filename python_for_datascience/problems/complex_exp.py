# Given data
snake_case_str = "snake_case"

# Write your code here

n=snake_case_str.split("_")
str=""
for i in n:
    str+=i.title()
print(str)


