# Write your code here
# Write your code here
row, column = map(int, input().split())
matrix1 = []

for i in range(row):
    row_values = list(map(int, input().split()))
    matrix1.append(row_values)

row1, column1 = map(int, input().split())
matrix2 = []

for i in range(row1):
    row_values1 = list(map(int, input().split()))
    matrix2.append(row_values1)

for i in range(row):
    matrix3 = []

    for j in range(column1):
        res = 0

        for k in range(row1):
            res += matrix1[i][k] * matrix2[k][j]
        matrix3.append(res)
    print(*matrix3)