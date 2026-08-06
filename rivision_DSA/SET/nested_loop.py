for valuee in range (1,21):
    print('starting the table of ',valuee)
    for i in range(1,11):
        print(valuee*i,end=' ')
    print()
print('usning while loop ',end='')

value=1
while value<=21:
    i=1
    while i<=10:
        print(value*i,end=' ')
        i+=1
    value+=1
    print()
