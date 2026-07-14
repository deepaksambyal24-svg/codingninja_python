def check_prime(n):
    i=2
    while (i*i)<=n:  # n sqare is user by i2
        if (n%i)==0:
            return False
    return True