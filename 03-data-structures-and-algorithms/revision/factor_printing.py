number=int(input('enter a number'))
isprime=True
for num in range (2,number):
    if number%num==0:
        print(num,end=' ')
        isprime=False


if isprime  :
    print('prime')