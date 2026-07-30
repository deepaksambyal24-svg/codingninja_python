# in this formulae is to print 'A + i-2


# is to print 'A+K-1
# WHEN WE STORE A CHAR IN COMPUTER WE STORE ASCII VALUE FOR THAT CHAR

# find ascii of A
# ADD K-1 IN INT
# FIND CHAR CORESSPONDINGLY

# print(ord('b'))
# print(chr(66))


# get the kth char in the alphabeet


k=int(input())
x=ord('A')
asciiTarget=x+k-1
tartchar=chr(asciiTarget)
print(tartchar)

n=int(input())
i=1
while i<=n:
    j=1

    while j<=n:
        charp = chr(ord('A') + j - 1)
        print(charp,end="")
        j=j+1
    print()
    i=i+1
