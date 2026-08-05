def user_activity():
    return "activity1",'activity2','activity3','activity4'
activity_tuple = user_activity()
print(activity_tuple)
print(type(activity_tuple))   # it pack the value in a tuple and return the values

# we can apply indexing on the value function returned

print(activity_tuple[0])
print(activity_tuple[1])
print(activity_tuple[2])

# unpacking ----> it stores multiple variable  also called destructuring
act1,act2,act3,act4 = user_activity()
print(act1)
print(act2)
print(act3)

# assign value to only one varibale and remaining value to another variable
v,*rest = user_activity()
print(v)            # only first variable return tuple 
print(rest)   # remaining variable stored in list
