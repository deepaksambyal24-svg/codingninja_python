n=int(input())
ans=("")
while n>0:
    if n%2==0:
        ans="0"+ans

    else :
        ans="1"+ans
    n=n//2
print(ans)
print(bin(int(ans)))