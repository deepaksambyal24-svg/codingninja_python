n=int(input())
i=1
p = i
while i<=n:
    j=1

    while j<=i:
        print(p,end=" ")
        j=j+1
        p+=1
    i=i+1

    print()