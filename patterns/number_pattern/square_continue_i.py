n=int(input())
i=1
p=1
while i<=n:
    j=1
    while j<=i:
        print(p,end=' ')
        p=p+1
        j=j+1
    i=i+1
    print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10