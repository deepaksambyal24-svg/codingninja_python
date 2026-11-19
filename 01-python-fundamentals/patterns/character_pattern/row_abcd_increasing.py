n = int(input())
i=1

while i<=n:
    j=1
    starchar= chr(ord ('A')+i-1)
    while j<=n:
        charp= chr(ord(starchar)+j-1).upper()
        print(charp,end='')
        j=j+1
    i=i+1
    print()
# ABCD
# BCDE
# CDEF
# DEFG