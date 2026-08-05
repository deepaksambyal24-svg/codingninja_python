# GENERATOR ----> It give values one at a time , instead of creating and sorting all value together
a=[x*x for x in range(1,10)]
print(a)

# syntax for a gernator ---> when the data is large ,  we dont need all results at the same time
# we want to same memeory we process one by one

# eg ----> generate monthly emi values
monthly_emi=8500
emi_schedule =(f'month{month}:emi:{monthly_emi}' for month in range(1,13))
for p in emi_schedule:
    print(p)


# filter high value transaction
transactions=[12000,68000,45000,95000,22000,71000]
high_value_txn=(amount for amount in transactions if amount > 50000)
for amount in high_value_txn:
    print("high value txn:",amount)


# nested for loop :
# syntax ---->
# for inner_loop:
        # for inner loop :
        #     print()

branches=['delhi','mumbai','chennai']
products =['laptop','mobile','tablet']
for b in branches:
    for p in products:
        print(b,p,end='\t'  )


# employee shift allocation
shift=['A','B','C','D','E','F']
empoyees=['1','2','3','4','5','6','7','8','9']
for p in empoyees:
    for b in shift:
        print(p,"can be assigned to",b,"shift")


#   permissible shifts to specific employees
# shifts=['morning','evening','afternoon','night']
# empoyees=['amit':['morning','evening'],'neha':['evening'','night'],'rahul':['morning','night']]
# for p in empoyees:


#---------------------------------------------------------------------------------------------------------


# WHILE LOOP ---->