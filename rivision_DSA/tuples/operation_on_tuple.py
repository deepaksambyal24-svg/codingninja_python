# tuples are immutable so we have create a new tuple to manipulate the tuple
tup=(1,2,3,4)
mutalble=list(tup)
print(mutalble)
mutalble[0]=5

user_activity=tuple(mutalble)
print(user_activity)


# string support += but tuple not support this
# because string create a brand new swting for concatination
