def count_ch_frequency(s,ch):
    count = 0
    for current_letter in s:
        if current_letter == ch:
            count += 1
        return  count