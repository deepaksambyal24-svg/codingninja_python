# it start with 0 1 1 2 3 4 5 8 13 ....
# 0+1=1
# 1+1=2
# 2+3 =5
n=int(input())
last_number=0
second_last=1
while n>=0:
    fibo= last_number+second_last
    print(fibo,end=" ")
    second_last = last_number
    last_number=fibo
    n-=1


