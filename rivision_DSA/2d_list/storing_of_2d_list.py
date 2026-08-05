# 2d list ---> it is the list of list
li=[[1,2,3],[4,5,6],[7,8,9]]
print(id(li))
print(id(li[0]))
print(id(li[1]))

# so it has different location has different id  so 2d list store the ref of differeent list
print(li[2])
not_2d_list=[[1,2,3],'addepak']  # it is a list of list and string not 2d list
