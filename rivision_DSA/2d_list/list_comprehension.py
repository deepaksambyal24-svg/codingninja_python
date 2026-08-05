li=[1,2,4,5]
square=[x**2 for x in li]
print(square)
# list comprehension is used for better code readability and much cleaner code

# list comprehension with condition
li_even_squares=[x**2 for x in li if x%2==0]
print(li_even_squares)




# list conprehension with if nested condition
li_new2=[x**2 for x in li if x%2==0 if x%3==1]
print(li_new2)



# find commmon element in two list ie intersectio of two lists


li_1=[1,2,3,4,5,6]
li_2=[1,2,8,9,4,5,6]
interection_list=[]
for ele in li_1:
    for ele2 in li_2:
        if ele==ele2:
            interection_list.append(ele)
print(interection_list)

# using list comprehension
li_int=[ele for ele in li_1  for ele_2 in li_2  if ele==ele2]
print(li_int)



# list comprehension using if else condition
li=[1,2,3,4,5,6]
li_int=[ele**2  if ele%2==0 else ele for ele in li ]


# how to generate a list of list using list comprehension


s='deepak'
li=[ele for ele in s ]
print(li)


# gernerate 2d list using list comprehenion

li=['ddepak','singh','paridkh']
ll_2d=[[s for s in ele] for ele in li]
print(ll_2d)