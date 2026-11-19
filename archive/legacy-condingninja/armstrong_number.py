def count_function(n):
    x=0
    while n>0:
        x+=1
        n//=10
    return x
def armstrong_number(number):
    num=count_function(number)
    temp=number

    while number>0:
        rem=number%10
        num+=rem**num

    return temp==num





