# when we store a vlue in character i python is store in ascii values
# 'A' is 66 , funciton ord and char are used to retrieve the ascii for char of a input
# ord is for single char length only it does not work for string
n = int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        charp= chr(ord('a')+j-1).upper()
        print(charp,end='')
        j=j+1
    i=i+1
    print()