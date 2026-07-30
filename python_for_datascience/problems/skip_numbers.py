# Write your code here
n=int(input())
if 1<=n<=999 :
    for num in range (1,n+1):
        if num%5==0 :
            continue
        if num==3 or num%10 ==3:
            continue



        print(num)