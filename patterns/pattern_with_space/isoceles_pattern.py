n=int(input())
i=1
while i<=n:
    # spaces

    space=1
    while space<=n-i:
        print(" ",end="")
        space=space+1
    #increasing sequece
    p=1
    j=1
    while j<=i:
        print(p,end="")
        p+=1
        j=j+1
    #decreasing sequence
    p=i-1                   #increasing number for row number from i-1 and so on
    print()                 #and till the 1  we decrease the dp for every iteration
    while p>=1:
        print(p,end="")
        p-=1
    print()
    i=i+1