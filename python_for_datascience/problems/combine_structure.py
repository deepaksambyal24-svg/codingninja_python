list_var = [1, 2, 3, 4, 5]

tuple_var = (6, 7, 8, 9, 10)

set_var = {1, 2, 3, 4, 5}

dict_var = {'a': 1, 'b': 2, 'c': 3}

def list_converter(li):
    li=list(li)
    return li

def add_var(li1,li2):
    return li1 + li2



def add_list(li1,li2):
    return li1 + li2

print(f'list_var:{add_var(list_var,list_converter(tuple_var))}')
print(f'set_var:{set((add_var(list_var,list_converter(tuple_var))))}')
print(dict_var)

dict_var['d']=min(tuple_var)
dict_var['e']=max(tuple_var)
print(f'dict_var:{dict_var}')