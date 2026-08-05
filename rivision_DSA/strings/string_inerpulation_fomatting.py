email='sanket@gmail.com'
password='sanket123'
comb='the email is '+email+' and password is '+password
print(comb)

# string interpulation --->%s,%s and then pass the argument

combb='the email of user is %s and password is %s'%(email,password)
print(combb)

value =12.3344
s='the value is %.2f'%value
print(s)


# format function
c='the email of user is :{} and password is :{}'.format('sanket',password)
print(c)
c1='the email of user is :{1} and password is :{0}'.format('sanket',password)
print(c1)
print(c)

# and other way to formating

s=f'the email of user is {email} and password is {password}'
print(s)
