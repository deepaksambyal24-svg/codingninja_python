def check_prime(num):
    for n in range (2,num):
        if num%n==0:
            return False
    return True
check = check_prime(2)
print(check)