def unique_vowels9(inp):
    result =set()
    vowels={"a","e","i","o","u"}
    for i in range (0,len(inp)):
        if inp[i] in vowels:
            result.add(inp[i])
    return result
print(unique_vowels9("deepak"))
