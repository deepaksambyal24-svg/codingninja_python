# Write your code here
binary=input()
binary=int(binary)

deci=0
pow=0
for i in str(binary):
    deci += 2 ** pow
    pow += 1
print(deci)





