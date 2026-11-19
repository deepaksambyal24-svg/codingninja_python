# FIBO--> 0,1,1,2,3,5,8,13____________
number=int(input("Enter a number: "))
second_last=0
last_number=1
print(second_last,end=' ')
print(last_number,end=' ')
counter=2
while counter<=number:
    next_fib=second_last+last_number
    second_last=last_number
    last_number=next_fib

    print(next_fib,end=' ')
    counter+=1
