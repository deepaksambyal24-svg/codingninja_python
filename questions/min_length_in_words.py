s = input()

words = s.split()

min_word = words[0]

for w in words:
    if len(w) < len(min_word):
        min_word = w

print(min_word)