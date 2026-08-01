freq_dict = {33: 2, 91: 4, 5: 1, 20: 3, 4: 0}
for value, freq in freq_dict.items():
    while freq_dict[value] < 0:
        freq_dict.append(value)
print(dict(sorted(freq_dict.items())))
