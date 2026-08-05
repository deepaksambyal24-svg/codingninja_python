# formula to access a element in 2d array is m*i+j
# where i is row j is column m is the no of column



# this is applicable for normal list
list=[[1,2,3],[4,5,6],[7,8,9]]
n=3
m=3
for i in range(n):
    for j in range(m):
        print(list[i][j],end=" ")

    print()

# for printing the jagged list
jagged_list=[[1,2],[4,5,6,9,50],[7,8]]

for row in jagged_list:
    for elem in row:
        print(elem,end=" ")
    print()

# 3rd way of printing using join function ()    ---


j='avc'.join("abcd")
print(j)


j1='avc'.join(['1','2','3','4','5','6','7','8','9'])
print(j1)

# printing list with join
list=[[1,2,3],[4,5,6],[7,8,9]]
n=3
for row in list:
    output=' '.join([str(elem) for elem in row])
    print(output)