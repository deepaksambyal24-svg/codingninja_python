# LOOPING STATEMENT ------->loops repeat the same block of code in python for n number of times we want
# same action must be repeated , every item in a collection must be executed
# TYPES OF  LOOPS ---->
# for loop
# while loop

# FOR LOOP Is used when we have a sequence or generally we know how many times it will be executed
# it goes through itmes one by one . used i list strings sets and range of values



# WHILE LOOP ----> When repetation depends on a condition ,continues whilie a condition remains true
# when the number of repetatin is uncertain




#----------------------------------------------------------------------------------------------------
#FOR LOOP -----> Takes item from a collection one at a time
# SYNTAX ---- for item in sequence:
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit,end='\t')

empl=['a','b','c']
for emp in empl:
    print( "happy diwali !!!",emp)


# combining for loop with if -else
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,191,]
for n in a:
    if n%2==0:
        print(n,end='\t')


#Add values in a list using lopp
num=[1000,2222,13333,55555]
sum= 0
for n in num:
    sum+=n
print(sum)


l=[30,50,1000,50]
m=[]
for n in l:
    m.append(n)
print(m)

# for loop with if ----
l=[22,33,44,55,66]
m=[]
for n in l:
    if n>45:
        m.append(n)
print(m)


# string  for loop ----> remove duplicate character from a string

a ="aabbbcccdddd"
b=""
for n in a:
    if  n not in b:
        b+=n
print(b)


#   RANGE ------range () funciton it produces a sequence of number
## range (5) ------> 0 to 4    range (start,stop,step)

for item in range (16):
    print(item,end='\t')

for c in range(10,21,2) :
    print(c,end='\t')

for c in range (20,9,-1):
    print(c,end='\n' )


#ENUMERATE FUNCTION ---- > enumerate() : this function shows the position of as well as their respective itmes together
fruits = ['apple', 'banana', 'orange']
for i , j in enumerate(fruits,start=1):
    print(i,j)



## else with for loop : ---> print all numbers from 1 to 10 and after that print as mission successful
for b in range(1,11):
    print(b,end=' ')
else:
    print('not eligible')


# LIST comprehension --- > its a compact way to : loop through the values , optionaly filterthem , transform them
# place the result into a new lis t
# syntax ---> variable =[expression for item in iterable]

price=[100,200,300,500]
tax=[]
x=[i*.18+i for i in price]
print(x)

# list comprehension with condition

# syntax ---> [expressin ofr item in iterable if condition ]
even =[x for x in range(1,21) if x%2==0]
odd =[x for x in range(1,21) if x%2!=0]
print(even)
print(odd)


# list conprehension with if else
# syntax ---> a=[true_vale if condition else false_value for item in iterable]

f=['banana','cherry','kiwi']
final=[x if x!='banana' else 'orange' for x in f]  # we can use replace a value in list 
print(final)




# ---------------------------------------------------------------------------------------------
# WHILE LOOP -----> It is used when repeatations depends on condition

# syntax ----->
# while condition :
        # codeblock

i=1
while i<10:
    print(i,end='\t')
    i=i+1

# sell all products till they become out of stock

stock=5
while stock>0:
     print('one product sold')
     stock-=1
     print('remaining stock:',stock)


# process customers waiting in a queue
customer_no=4
ticket_number=4
while  customer_no>0:
    print("ticket number:",ticket_number)

    print("remaining ticket number:",ticket_number)
    customer_no-=1
    ticket_number += 1
    print("customer still waiting ",customer_no)


# while with else
# while condition syntax ---->
# while condition:
        # else : cod e



# conpleation  of loan repayment
loan_balance=30000
monthly_pay=1000
month=1
while loan_balance>0:
    print('month',month,'payment',monthly_pay )
    loan_balance-=monthly_pay
    print('remainining monthly_pay:',loan_balance   )
    month+=1
else:
    print('loan fully paid')

# nested while loop ---->
#syntax ---> while outer :
#                   inner while :



zip_ N