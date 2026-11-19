def count_ch_frequency(s,ch):
    idx=0
    count=0
    while idx<len(s):
        if s[idx]==ch:
            count+=1

            idx+=1
    return count
my= count_ch_frequency("deepak","e")
print(my)
