
number =int(input())
reminder=0
while number>0:
    rem = number  %10
    print(rem,end="")
    number//=10