def unique_elements(input_tuple):

    result=[]
    for element in input_tuple:
        if element not in result:
            result.append(element)
    return tuple(result)
print(unique_elements((1,2,3)))
