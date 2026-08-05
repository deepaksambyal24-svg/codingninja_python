from prompt_toolkit.key_binding.bindings.named_commands import capitalize_word

row=int(input())
column=int(input())
matrix=[]

for i in range(row):
    current_row=[]
    for j in range(column):
          value=list(map(int,input().split()))
          current_row.append(value)
    matrix.append(current_row)

print(matrix)
print(matrix[0][0],matrix[1][0])
capitalize_word("the workd")