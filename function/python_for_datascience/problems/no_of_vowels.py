vowels=['a','e','i','o','u']
count=0
inp="hello world"
# Write your code here

li=map(str,inp.split())
for i in li:
   for ch in i:
       if ch in vowels:
           count+=1
       else:
           continue
print(count)