import sys
input = lambda:
(sys.stdin.readline().rstrip("\r\n"))

import sys

input = lambda: (sys.stdin.readline().rstrip("\r\n")
# Don't make changes to the above lines
string1 = input()
string2 = input()
# Write your code here

s1 = string1.replace(" ", "").lower()
s2 = string2.replace(" ", "").lower()
sorted1 = sorted(s1)
sorted2 = sorted(s2)
print(sorted1 == sorted2)
