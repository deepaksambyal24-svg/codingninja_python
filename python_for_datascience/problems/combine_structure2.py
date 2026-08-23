list_var = [1, 2, 3, 4, 5]
tuple_var = (6, 7, 8, 9, 10)
set_var = {1, 2, 3, 4, 5}
dict_var = {'a': 1, 'b': 2, 'c': 3}


list_var+=list(set_var)
list_var=list(set(list_var))
print(f'list_var: {list_var}')

