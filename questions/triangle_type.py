# Write your code here
x = int(input())
y = int(input())
z = int(input())
if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("Equilateral Triangle")
    elif x == y or y == z or z == x:
        print('Isosceles Triangle')

    elif x != y and y != z and z != x:
        print('Scalene Triangle')
else:
    print("Not a Triangle")
