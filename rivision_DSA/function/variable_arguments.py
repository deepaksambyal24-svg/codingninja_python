# when dont know the exact number of arguments  and is knows as variable arguments
# TWO TYPES------> *args

def sum_of_number(*numbers):
    return sum(numbers)


#   **KWARGS -----> WHEN YOU PASS THE VALUE KEY VALUE PAIRS
def print_details(**details):
    print(details)
print_details(name:='deepak',company='micor')   