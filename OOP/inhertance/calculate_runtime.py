import time
def calculate_runtime(func):
    def innter(arr):
        start_time = time.time()
        result = func(arr)
        end_time = time.time()
        print( "runtime is", end_time - start_time)
        return result
    return innter
@calculate_runtime
def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
arr= [ 1,3,5,6,7,8,8]
print(sum(arr))
