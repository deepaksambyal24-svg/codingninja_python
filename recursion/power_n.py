def power(x,n):
    if n == 0:
        return 1
    output= power(x,n-1)
    return output*x
print(power(3,4))