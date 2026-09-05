inpu="19823456"
even=[]
odd=[]
for digit in inpu:
    if int(digit)%2==0 :
        even.append(digit)

    else:
        odd.append(digit)

a=(sorted(even))
b=(sorted(odd))
final=b+a
print(*final)