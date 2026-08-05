def count_char_freq(str, ch):
    idx=0
    count=0

    while idx < len(str):
        if str[idx] == ch:
            count += 1
        idx+=1
        return count

count = count_char_freq('deepak', 'a')
print(count)