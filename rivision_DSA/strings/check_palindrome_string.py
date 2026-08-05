def check_palindrome(s):
   n=len(s)
   i=0
   j=n-1
   while i<j:
       if s[i]!=s[j]:
           return False
           i=i+1
           j=j-1
       else:
           return True

print(check_palindrome('aba'))
print(check_palindrome('aab'))


