from operator import truediv


def find_n_in_array(arr,x):
    if len(arr) == 0:
        return False
    if arr[0] == x:
        return True
    return find_n_in_array(arr[1:],x)

