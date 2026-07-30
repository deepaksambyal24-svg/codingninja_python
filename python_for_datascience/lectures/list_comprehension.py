#list comprehension ---> it is shorter way to create a list
# it usually combines a loop ,an operation , sometimes a condition
a = { 1,2,3,4,5 }    # now i want to store square of all element and store to another list

# syntax   ---> expression of item in collection
b=[]
for i in a:
    b.append(i**2)
print(b)


# by using list comprehensive

b=[n**2 for n in a]
print(b)

prices=[1000,2000,3000,4000,5000,6000]
c=[price+1.8*price for price in prices]
print(c)


# expression for item in collection if condition
sales=[45000,50000,60000,70000,80000,90000,100000]
c=[n for n in sales if n>60000]
print(c)

prices=[500,1200,2500,800,1800]
discount=[n*0.9 for n in prices if n>1000]
print(discount)

 