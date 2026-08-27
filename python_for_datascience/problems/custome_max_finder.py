# Given data
data = [2000, 5890, 876, 1289, 3009]

max_element = data[0]  # Assume the first element is the maximum

for num in data:

    if num > max_element:
        max_element = num

    else:
        continue
print(max_element)


