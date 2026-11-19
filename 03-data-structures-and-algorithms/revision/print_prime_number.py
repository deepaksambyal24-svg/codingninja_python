number=int(input("Enter a number: "))
i=2
while i<number-1:
    if number%i==0:

        print("this is the composite number")
        break
    else:

        print("this is the prime number")
        break

# number=int(input("Enter a number: "))
# i=2
# isprime=True
# while i<number-1:
#     if number%i==0:
#         isprime=False
#         break
#     i+=1
# if isprime:
#     print("prime number")
# else:
#     print("not prime")