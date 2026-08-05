# METHODS IN FUNCTIONS
email ='sanket@gmail.com'
print(email.upper())  # it does not change the actual string it create a brand new upper char string


# split function ---> it divide or tokenize individual char

name ='deepak singh'
print(name.split(" "))


#join function

print("#".join(name))

# find function
password='sanket123'
print(password.find("12"))

# comparison of two sub strings

print (password=="")
word ='abc'
print(word.isalnum())
print(word.isalpha())
print(word<'abc')           # check the dictionary order

print(word.isalnum())
print(word.isalpha())