
def check_palindrome(s):
    n= len(s)
    i=0
    j=n-1 # n-1 is the last or rightmose index
    while i<=j:
        if s[i]!=s[j]:
            print('Palindrome')
        else:
            print('Not Palindrome')
        i+=1
        j-=1


check_palindrome('cda')



