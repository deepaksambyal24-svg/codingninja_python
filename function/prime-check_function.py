def is_prime(n):
    if n <=1:
        return False
    j=2
    count=0
    while j<n:
        if n%j==0:
            isprime=False
        j+=1
        count+=1
    return count
my =is_prime(2)
print(my)dd


