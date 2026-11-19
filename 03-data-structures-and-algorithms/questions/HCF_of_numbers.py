a, b = map(int, input().split())

if num1 < num2:
    small = num1
else:
    small = num2

hcf = 1

for i in range(1, small + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print(hcf)
