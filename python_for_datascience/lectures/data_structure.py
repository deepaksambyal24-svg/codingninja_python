# Data Structures-->
#FOR EFFICIENCY --> memory management ,FLEXIBILITY--> different types of data types
# ABSTRACTION--> hiding internal complex details
# SCALABILITY--> even if data size grows it has the capacity to store all of them
# ORGANIZED --> storing all values in proper sequence

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# LIST--> it is an ordered and changeable collection of items.all elements are written within
# square bracket [] separated by comma it can also store data of multiple of type

'''PROPERTIES OF LIST
ordered --> each item has its fixed index position
mutable--> lists can be modified

'''


a=[1,2,3,4,5]
b=["apple",123,True,22.6]
a[0]='banana'  # change the element
print(a)
d=[123,"charlie",'apple',"banana"]
c=[1,2,3,4]


# LIST CONSTRUCTOR --> It converts one data type into another --list()
print(list(a))


# NESTED LIST--> one list within another
m=[[1,2,3,4,5],['apple',123,True,22.6],['fox','cat','dog']]
print(m)
print(m[0][2]) # access element form nested list

#accessing the items --> by indexing
fruits=['apple','banana','pear','orange']
print(fruits[-1])
print(fruits[-1:-3:-1])

# slicing
print(fruits[:2])

# len() --> how many items are there in a list
nested=[1,2,3,[4,5,5],[a,b,c]]
print(len(nested))

# max and min --> finding the largest and the smallest elements within a list
marks =[10,25,59,90,True]
print(max(marks))
print(min(marks)) # True means 1 and False means 0 so min is True
print(sum(marks))
text=['abc','abd','abe'] # alphabatically sorted for checkin
print(min(text))

# changing range of items in a list
a=['apple','date',999.0988,'g@mail']
a[1:4]=['def']
print(a)
b[1:4]=[20,30,40]
print(b)

# HOW TO REPEAT A LIST
numbers=[1,2,3,4,5]
print(numbers*4) #  print the list four times


# append - adding item in the list
numbers.append(6)
print(numbers)

# extend -it add multiple items at the end of list
numbers.extend([7,8,9])
print(numbers)
# also used to add element from one list to another list
nun2=[11,12,13]
numbers.extend(nun2)
print(numbers)

#INSERT--> add items based on position
numbers.insert(1,100)
print(numbers)

#   "+" --> OPERATOR  THIS OPERATOR IS USED FOR COMBINING THE LIST
school=['school','college','university']
fees=[100000,444444,9999]
new=fees+school
print(new)


# COMPARING LIST --> Using the camparison operator "=='", first it compare the value then the size of list

a=[1,2,3,4,5]
b=[9,10,10,11]
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
# REMOVE (): remove the value
a=['apple','banana','pear','orange']
a.remove('pear')
print(a)

# P0P--> remove an item by index and also returns it, POP return the remove last element
a.pop()
print(a)
a.pop(0)
print(a)


# DEL--> delete item at any index, del return nothing
s=[a,b,c,d]
del s[2]
print(s)

# CLEAR--> it removes all the items and return the emply list
s.clear()
print(s)


# SORTING --> We can sort a list using sort()
numbers=[1,6,9,1,4,6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)  # for desc order use this
print(numbers)

#joining LIST  items using join () function
# join() --> is the method to joins list items into string  it only works with strings
string=['hello','world', 'here']
x='@'.join(string)
print(x)
a=['p','y','t','h','o','n']
d=''.join(a)   # delimiter is mandatory for joins
print(d)

# counting occurences --> how many times an items occuring in the list
n=[1,2,3,4,4,3,55,4]
print(n.count(4))   # --> gives the occurences of item in list hence return 3


# COPY--> Coping means create separate duplicate list
# copy() method
a=[1,2,3,4,5,6]
b=a.copy()
print(b)

# by using the slicing
c=a[:]
print(c)


# INDEX () --> USE TO GET THE POSITION OF  AN ITEM -->  index ()
print(c.index(6))


# REVERSE A LIST BY USING reverse () function
a.reverse()
print(a)    # --> reverse the list
#-===================================================================================================================
# MAP FUNCTION --> the map() function is a build in python function used to apply the function to every element of an iterable list
# SYNTAX --> map(function,iterable )  function is the a function to apply and iterable is a list tuple set string


# eg ------> square of every number -->
numbers=[1,2,3,4,5]
squared_numbers=list(map(lambda x: x**2, numbers))
print(squared_numbers)
# here lambda is the  an anonymous unnamed function  here x is the parameter and x**2 is the expressionn
# it means take one value  called x and return its sqaure

# CONVERT strings to uppercase
fruits=['apple','banana','pear','orange']
result=map(str.upper,fruits)
print(result)



# convert strings to integers
numbers=[1,2,3,4,5,6]
result=map(int,numbers)
print(result)



def cube(x):
    return x**3
numbers=[1,2,3,4,5]
result=map(cube,numbers)
print(list(result))

#=======================================================================================================================

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


#TUPLE-->it is also a collection of data . tuples are immutable  written inside () and all items are
# separated by , " comma" , it also allow dupliates and store multiple data type in a single list,,
# also for a tuple we have atleast two elements inside the bracket

days=("mon","tue","wed","thu","fri","sat","sun")
student=('amit',21,81.5,True)
a=1,2,3 # ---> THIS IS ALSO A TUPLE BOTH WITH BRAKCET OR WITHOUT BRACKET
print(a)
print(student)


# tuple constructor -->  it change or covert a list frm a list to a tuple
a=['apple','banana','pear','orange']
c=tuple(a)  # --> convert list into tuple
print(c)


 # convert string into tuple
s=("data science")
t=tuple(s)
print(t)


# ordered --> tuple has also indexing from 0 so slicing operation can be done on tuple


# NESTED TUPLE --> Tuple inside a tuple is called a nested tuple
n=((1,2),(3,4),(5,6),(True,False))
print(n[0])  # it gives (1,2)
print(n[2][1])
print(n[-2])
print(n[:2])


# TUPLE IMMUTABILITY --> How to change elements inside a tuple

a=(1,2,[3,4])  # tuple inside the tuple
a[2].append(5)  # --------> append the 5 element inside the list inside a tuple
print(a)

#REASSIGN A TUPLE
t=(1,2,3,4,5)
t=(33,4,5,6)
print(t)     # reassignment of value inside a tuple

s=list(t)   # convert the tuple into list and then remove the element from tuple
s.remove(6)
print(s)
print(tuple(s))  # again converted to tuple

# JOINING TUPLES --> + is used to join tuple
t1=(1,2,3)
t2=('a','b','c')
result=t1+t2
print(result)
d =t+t
print(d)

# example
a =(7,)
v=(1,3,4)
d=a+v   # it gives string concate error because a has only 01 item so for tuple we have to write comma at last
print(d)



# COUNT --> COUNT THE NUMBER OF OCCURENCE OF AN ITEM IN A TUPLE
a=(1,2,2,23,4,2,4,5)
print(a.count(4))

# index --> gives the index position of any element inside the tuple
a = ('watch',"bag",'hi',100,24,True)
print(a.index(100))


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#SET
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#DICTIONARY
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# STRING
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
