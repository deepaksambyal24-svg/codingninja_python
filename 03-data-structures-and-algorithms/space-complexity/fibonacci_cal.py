def calc_fibonacci(n):
    #calculate the nth fibonacci
    if n==0 or n==1:
         return n
    fib_arr= [0,1]
    for i in range (2,n+1):
        fib_arr.append(fib_arr[i-1]+fib_arr[i-2])
    return fib_arr[n]   #the nth fib is at the nth index


print(calc_fibonacci(9))


# another function for fibonacci calculation not using extra spaces
def calc_fib(n):
    if n==0 or n==1:
        return n
    last_num=0
    iindlast_num=1
    fib_num=None
    for i in range(2,n+1):
        fib_num=last_num+iindlast_num
        last_num=fib_num
        iindlast_num=last_num
    return fib_num

print(calc_fib(9))