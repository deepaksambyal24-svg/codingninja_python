a="1234"
b="3456"

set_a=set(a)
set_b=set(b)
ans=sorted(((set_a|set_b)-(set_a & set_b)))
print("".join(ans) )# Write your code here

a= input()
b=input()
set_a = set(map(int, a.split()))
set_b = set(map(int, b.split()))
if set_a==set_b:
    print("No symmetric difference")
else:




        ans=sorted((set_a|set_b)-(set_a & set_b))

        print(*ans)