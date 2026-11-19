def printTable(start, end, step):
    for f in range(start, end + 1, step):
        c = (f - 32) * 5 // 9
        print(f, c)
result= printTable(36,618,78)
print(result)