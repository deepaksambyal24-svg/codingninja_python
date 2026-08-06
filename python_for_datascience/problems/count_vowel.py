


def count_vowels(s):
    count = 0
    for char in s:
        if char in 'aeiou':
            count+=1
            return count

print(count_vowels("aeiou"))
print(count_vowels("hello"))