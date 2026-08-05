# string are immutable so whle concate two string it create a brand new string and put items of both string
user='deepk'
email='deepakaksjljal;'
full=user+email
print(full)
print(id(full))
print(id(user))