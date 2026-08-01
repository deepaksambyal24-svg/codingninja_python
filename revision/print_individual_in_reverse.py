number=12345
digit=" "
print(number//10)
print(number%10)
while number>0:
     remainder=number%10
     print(remainder,end=' ')
     number//=10

