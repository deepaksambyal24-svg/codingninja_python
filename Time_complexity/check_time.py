import time

start = time.perf_counter()

print("hello world")
print("hello world")
print("hello world")

end = time.perf_counter()

print("Execution time:", end - start)