# Given data
marks = "56 78 94 85 62"
marks = marks.replace('94', '49')
# Write your code here
marks = list(map(int, marks.split()))
sum = 0
for i in marks:
    sum += i
print(f'Correct Average: {sum / len(marks)}')
