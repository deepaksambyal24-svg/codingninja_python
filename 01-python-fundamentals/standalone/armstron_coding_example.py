from subprocess import run




def count_digits(n):
    result=0
    while n>0:
        result+=1
        n=n//10
    return result
def  check_armstrong(num):
    d= count_digits(num)
    sum_ofdigit_power=0
    temp = num
    while num>0:
        x = num%10
        sum_ofdigit_power+=x**d
        num=num//10
    return sum_ofdigit_power==temp

