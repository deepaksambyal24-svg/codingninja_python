
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    current_row=list(map(int,input().split()))
    matrix.append(current_row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=" ")
    print()