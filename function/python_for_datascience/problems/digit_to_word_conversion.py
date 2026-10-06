# Map digits to words
digit_to_word = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                 '8': 'eight', '9': 'nine'}

# Write your code here

inpu = "123"
res = ""
for char in inpu:
    if char in digit_to_word:
        res += digit_to_word[char]

print(res)