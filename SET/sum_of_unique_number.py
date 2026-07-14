def sum_of_unique_numbers(li):
    unique_numbers = set(li)
    result = 0
    for el in unique_numbers:
        result += el
    return result
print(sum_of_unique_numbers([1,2,3,4,5,6,7,8,9]))

#can also use sum funtion

def sum_of_unique_numbers(li):
    unique_numbers = set(li)
    return sum(unique_numbers)