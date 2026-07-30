# map() ---> applies the same function to every item in collection
# syntax ---> map(function,collection)
#every  function starts with word def ()
a=(1,3,4,5)
def square(num):
    return num**2

result=tuple(map(square,a))
print(result)

salaries =(40000,50000,60000,70000)
# apply 10 percent increment on each salaries
def increment (salary):
    return salary+.1*salary

result=tuple(map(increment,salaries))
print(result)


# when to use list  []
# order matters ---> use list
# have duplicate values ---> use list
# when we want to tamper the data


# when to use tuple   ()
# when order matters
# you dont want to tamper the data


# when to use set :  {}
# when you want to do data cleaning for removing duplicates
# order  doesnot matter
# when members are to be testee



# when to use dictionary    {]
# where value has a meaning labell
# where we want to change the data
# if parts of informatin we want to extract instead of all them together
