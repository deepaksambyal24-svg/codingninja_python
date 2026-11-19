li_1=[1,2,3,4,5]
li_2=[1,4,6]
int_li=[]
for ele in li_1:
    for ele_2 in li_2:
        if ele==ele_2:
            int_li.append(ele)
print(int_li)

li_inter_line= [ele for ele in li_1 for ele_2 in li_2 if ele==ele_2]
print(li_inter_line)

## sytex i s [ output, for -expression, conditinals]

# li_sqare_if=[ele**2 for ele in li_1 if ele==ele_2 else for ele in li_2]
# print(li_sqare_if)