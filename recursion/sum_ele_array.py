def sumArray(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sumArray(arr[1:])
