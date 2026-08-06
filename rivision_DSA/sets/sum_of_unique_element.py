# Q )     GIVEN A LIST OF NUMBERS ,RETURN SUM OF ALL THE UNIUE NO

A=[1,2,1,3,2,4]
temp=list(set(A))
sum=0
for i in temp:
    sum=sum+i
s=list(set(A))
print(sum)
