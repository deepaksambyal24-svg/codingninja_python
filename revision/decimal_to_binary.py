number =13
ans=""
while number>0:
    if number%2==0:
        ans="0" + ans
    else:
        ans="1" + ans
    number = number // 2
print(ans)
