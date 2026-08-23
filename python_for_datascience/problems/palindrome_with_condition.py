# Write your code here

str =  "A man a plan a canal Panama"


# Write your code here
str=input()
s=str.replace(" ","").lower()
if (s[::-1])==s:
    print(True)
else:
    print(False)