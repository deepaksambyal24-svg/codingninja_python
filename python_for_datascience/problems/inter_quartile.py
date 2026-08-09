


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_data = sorted(data)
if len(sorted_data) % 2 == 0:
      median=(sorted_data[len(sorted_data)//2]+sorted_data[len(sorted_data)//2-1])/2
      print(median)
else:
    median=sorted_data[len(sorted_data)//2]
    print(median)
lower_half=sorted_data[:int(len(sorted_data)/2)]
if len(lower_half) % 2 == 0:
    q1=(lower_half[len(lower_half)//2]+lower_half[len(lower_half)//2-1])/2
    print(q1)
else:
    q1=lower_half[len(lower_half)//2]
    print(q1)
if len(sorted_data) % 2 == 0:

    upper_half=sorted_data[int(len(sorted_data)/2):]

else :
    upper_half=sorted_data[int(len(sorted_data)/2)+1:]
if len(upper_half) % 2 == 0:
    q3=(upper_half[len(upper_half)//2]+upper_half[len(upper_half)//2-1])/2
    print(q3)
else:
    q3=upper_half[len(upper_half)//2]
    print(q3)

print(sorted_data)
print(median)
print(lower_half)
print(upper_half)
