n = 5
for i in range(1, n+1):
      if i % 2 == 0:
          print(f"{i} is even")
      else:
          print(f"{i} is odd")
else:
       print("For loop completed.")
while n > 0:
       if n % 2 == 0:
          print(f"{n} is even")
       else:
          print(f"{n} is odd")
       n -= 1
else:
       print("While loop completed.")

