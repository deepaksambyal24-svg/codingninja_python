n=int(input())
product=1
if n==0:
    print(1)
elif n<0:
    print("Error")

else:

    for i in range (n,1,-1):
        product*=i
    print(product)