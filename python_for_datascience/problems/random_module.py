import random


# Don't make any changes to the above line

def random_selection(arr, k):
    actual_list = arr[:]
    n = len(arr)
    if k > n:
        return -1

    random.shuffle(actual_list)
    ans = []
    for ele in range(0, k):
        ans.append(actual_list[ele])
    return ans


