bina=int(input("Enter a Binary Number: "))
power_of_2=2**0
ans=0
while bina>0:
    rem=bina%10
    ans+=rem*power_of_2
    bina=bina//10
    power_of_2*=2
print(ans)