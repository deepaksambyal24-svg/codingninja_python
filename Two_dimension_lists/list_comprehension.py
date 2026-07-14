li=[1,2,3,4]
li_new=[]
for ele in li:
    li_new.append(ele**2)
print(li_new)

li_new_c=[ele**2 for ele in li]
print(li_new_c)
li_new_even=[ele**2 for ele in li if ele%2==0]
li_new_odd=[ele**2 for ele in li if ele%2==0 if ele%3==0]
print(li_new_even)
print(li_new_even)




li_even_square_loop=[]
for ele in li:
    if ele%2==0:
        li_even_square_loop.append(ele**2)
