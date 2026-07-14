n=int(input())
power =0
number=0
while n>0:
    rem = n%10
    number+= rem* 2**power
    power= power+1
    n=n//10
print(number)

