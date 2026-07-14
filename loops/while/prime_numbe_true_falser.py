n  =int(input())
i =2
is_prime=True
while i<=n-1:
    if n%i==0:
        is_prime=False              # to know whether the loop break or exhausted
        break
    i=i+1
if is_prime:
    print("Prime")
else:
    print("Not prime")