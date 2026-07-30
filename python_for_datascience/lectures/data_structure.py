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
from jedi.inference.value import iterable
from prompt_toolkit.eventloop import async_generator

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
#SET :- SETS are unordered , sets are mutalbe , duplicates are not allowed and are represented
# by {} and each element inside the bracket separated by comma, sets dont have any index

# HOMOGENEOUS SET --> Same data type for all elements

fruits={"apple",'banana','pear','orange'}
print(fruits)
department={'hr','finance','sales','it'}
skills={'python','sql'}
skills.add('power bi')
print(skills)

# HETEROGENEOUS SET --> Multiple data type of elements
a ={10,'python',"True",(1,2)}

 # invalid set --> {[1,2,3]} --> a list cannot placed inside the set ,tuple can be,sets objet is not
 # subscriptable means  not ordered

 # duplicate value
a={1,3,3,2,4,1}
print(a)  # remove duplicate


# set constructor, dont use {} because it same as dictionaru always set()
b=set()
print(type(b))

# single -element set
s={42}
print(s)   #--> unlike tuple we can create a set with single element without comma

# converting list ot a set by set constructor
n=[1,2,33,4,3,1,2]
x=set(n)
print(x)  # it remobe duplicate from the list

# converting tuple to a set
t=(10,20,10,20,30)
x=set(t)
print(x)
# string conversion --> gives unordered char
a='hello'
b=set(a)
print(b)

# behaviour of BOOLEAN Data type in sets -->
x={False,0,True,1}
print(x) #-----> gives only true and false output


# what can be stored inside a SET -->LIST INSIDE THE SET ARE NOT ALLOWED , set required stable element for there
# internal searching system so a list cannot directly used as a set element , aset cannot directly contai another
# ordinary set  NESTED SET are not allowed
# {1,2,3,{4,5,6,7,},5,7}   -->not allowed

# FROZEN SETS :------> it is the immutable version of set , i canot add anything in a set
a={frozenset({1,2}),frozenset({3,4})}
print(a)

# accessing and examine set  items
fruits ={'apple','banana','pear','orange'}
print('banana' in fruits)
print('cherry' not in fruits)

# LENGTH FUNCTION --> len()

department = {'hr','finance','sales','it','hr'}   # --> does not include the duplicate values it give 4 in output
print(len(department))

# MAX VALUES
score ={78,89,50}
print(max(score))
print(min(score))
print(sum(score))

# add function add()    --- > add one item at items somewhere

skills={'python','sql','excel'}
skills.add('power bi')
print(skills)

# UPDATE --> add multiple values
# update([iterable])--->syntax ( iterable list,set ,tuple,dictionary,string o add multiple elements,
# Python needs something it can read one item at a time.

skills.update({'power','statistics','genai'})
print(skills)

# remove element from a set
#remove () delete a specific element

skills={'python','sql','excel'}
skills.remove('python')
print(skills)
print(skills)    # remove an item only when it exists other wise it give error
skills.discard('excel')  # it does not give error item not present and return actual set

# POP () --> remove and return the item
a=skills.pop()
print(a)

# clear() --> remove every item but structure still remains
skills.clear()
print(skills)  # --> give empty set

# del() --> it remove entire set even structure too and object
# del skills
# print(skills)


# SET OPERATIONS -->
#union----> return all the item from both sets only ones  --> opr -- ( | )
# intersection----> only common in both sets  ---> opr --(&)
# difference  ---> items which are present in one set and not in the second set --opr -- (-)
# symmetric difference---> items that belong to only one group but not both ---opr --- (^) unique in both group

python_student ={'amit',"neha",'rahul','sara'}
sql_student={'rahul','sara','john','meera'}
all_student=python_student | sql_student
all_student1=python_student.union(sql_student)
print(all_student)

# intersection
python_student.intersection(sql_student)
print(python_student)
all_student2=python_student & sql_student
print(all_student2)

# difference
difference=python_student.difference(sql_student)
difference=python_student-sql_student
print(difference)


# symmetric
sym=python_student.symmetric_difference(sql_student)
sym=python_student^sql_student
print(sym)

# UPDATE OPERATION METHODS --> all set operations using update basically modifies the original set
# eg - --> difference_update() , intersection_update() , symmetric_difference_update() , update()

a={1,2,3}
b={3,4,5}
a.difference_update(b)  # it change the values on the same time so difference will be stored in a
print(a)  # i


 # intersection_update
r={'amit','sara','johm','neha'}
s={'sara','john','rahul'}
r.intersection_update(s)  # store intersion ie sara john in variable in r
print(r)


# symmetric_update
x={'sara','deep','hi'}
y={'amit','john','rahul'}
x.symmetric_difference_update(y)
print(x)

# DISJOINT-----> isdisjoint () no common element . two sets are disjoint if there are no commanlity in betwwen
# them
a={'amit','neha','charlie'}
b={'rahul','john','gargi'}
isdisjoint=a.isdisjoint(b)
print(isdisjoint)

# ISSUBSET---> issubset() a set is a subset when all its element occur inside another set
a={'python','sql'}
b={'python','sql','bi','excel'}
print(a.issubset(b))

# ISSUPERSET() --> It contain all the element of a set (subset)
# in above case b is superset
print(b.issubset(a))

# COPY FUNCTION --> Copy a set to another set
original={'python','sql'}
copy=original.copy()
print(copy)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#DICTIONARY----->it follows key values pair . it store information as a key value written with the
# curly bracket
student={'name':'deepak','age':40,'blood group': 'ave'}
print(student.keys())
print(student.values())
print(student.items())
print(type(student))


# WHY DICT ARE REQUIRED :--> The meaning of element is store with its key value
# distionary are key-value pairs, mutable, does not allow duplicates for keys but value can have duplicate
product={101:'a',102:'b',103:'c'}
models={'brand':'ford','electric':False,"year":2020,"color":['red','white','black']}
print(models)
# RULES FOR DICT KEYS :----> keys have to be unique and hashable it means an object that has a fixed identity
# or value that python can convert into a number
# examples={'name':'amit',101:'employee', (2026,7):'july 2026'}--> give type error in (2026,7)
# grades ={('john','darry'):85,("alice","smitth"):92} ---> gives error not hashable


# dictionary constructore ---> dict()
data = [['a', 1], ['b', 2], ['c', 3]]

result = dict(data)

print(result)
print(type(result))

# nested dictionary one dictionary within another
students ={'student1':{'name':'alice',"age":20,'course':'computer'},'student2':{'name':'bob',"age":22,"course":'engineering'}}
print(students)


# LEN() ---> Count key value pairs in a dictionary
print(len(students))

# ACCESSSING ELEMENT FROM A LIST ---> get () function
student={'name':'rahul','age':20,'course':'computer'}
print(student.get('name'))
print(student.get('course'))

print(student.get('marks')) # key not exists
print(student.get('marks', 'not found')) # error handling

# get element from nested dictionary

students ={'student1':{'name':'alice',"age":20,'course':'computer'},'student2':{'name':'bob',"age":22,"course":'engineering'}}
print(students['student2']['course'])
print(students['student1']['course'])

# membership operator in dictionary
student={'name':'rahul','age':20,'course':'computer'}
print("name" not in student)


# keys () ---> return all keys from the dictionary
student={'name':'rahul','age':20,'course':'computer'}
print(student.keys())

# values () ----> return all values from the dictionary
print(student.values())


# items () ---> return all key value pair as a tuple
student={'name':'rahul','age':20,'course':'computer'}
print(student.items())

# changing dictionary values ---->
student={'name':'rahul','age':20,'course':'computer'}
# change city to pune
student['college']='engineering'
print(student)


#  update () ---> add or modify several key value pairs
b={'name': 'jullie',"age": 30}
b.update({'college':'engineering','city':'goa'} )
print(b)

# setdefault() -----> returns the value of a key if the key is absent , it creates that key with a default value
a={'name':'rohan','age':22}
result=a.setdefault('city','hyderabad')
print(result)

# REMOVING ITEMS FROM DICTIONARIES :--->

# pop()
student={'name':'rohan','age':22}
r=student.pop('name')
print(r)
print(student)   # remove both key and values from dictionary

# popitem() ---> remove and return the last key value pair in dictionary
student={'name':'rohan','age':22}
r=student.popitem()
print(r)
print(student)


# del () ---> it removes a particular pair from dictionary it return nothing
student={'name':'rohan','age':22}
del student['name']
print(student)

# clear () ----> delete all the items from dictionary but keep the structure of dictionary
student={'name':'rohan','age':22}
student.clear()
print(student)

# AGGREGATION IN DICTIONARY ----- >   MIN() ,MAX() ,SUM()
sales ={'january': 200000,"feb": 250000,'march': 4000000}
print(min(sales.values()))  # it give min of values
print(min(sales)) # return min of key
print(max(sales.values()))
print(max(sales))

print(sum(sales.values()))

#   ZIP () ---> This function combines corresponding elements from multiple iterables
a=['id','name','price']  # there are two lists one has key and other has the value part
b=[1,'laptop',5000]

c=zip(a,b)
print(list(zip(a,b)))
print(dict(zip(a,b)))

# copy () ---> create duplicate dictionaries copies
# original={'name":"depak","dept":"sales"}
#     copied =original.copy()


# shallow copy : creates a new outer dictionary but nested mutable objects may still be shared
o={'name':'amit',"skills":['python','sql']}
c=o.copy()
print(c)
c['skills'].append('power bi ') # nested list addres is not changed in ref that why it change the original dict
print(c)
print(o)

# deep copy -- > copy nested dictionary indipendentlhy


# from keys () ---> creates a new dictionary using a collection of keys
dept=['sales','hr','it','ops']
frinal =dict.fromkeys(dept,'not avail')  # all vales in list treated as keys default value NONE , BUT HER not avail
print(frinal)


# loops in dictionary ----> repeating same task multiple times

# loops through keys
employee={'id':101,'name':'riya','dept':'sales'}
for key in employee:  # print all key
    print(key)


for keys ,value in employee.items():
    print(keys,end=' ')
    print(value,end=' ')

    print(key,":",value)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# STRING
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
