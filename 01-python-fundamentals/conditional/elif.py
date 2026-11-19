# if a condition is true it does not check other conditon
x= int(input())
if x >= 90 and x <= 100:
    print("a")
elif x >= 80 and x <= 90:
    print("b")
elif x >= 70 and x <= 80:
    print("c")
else:
    print("d")