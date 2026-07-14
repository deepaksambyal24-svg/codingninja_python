def words_with_freq(sentence,k):
    if len (sentence)==0:
        return 

    list =sentence.split()
    freq_map = {}
    for word in list:
        if word in freq_map:
           freq_map[word] += 1
        else:
            freq_map[word] = 1
    for (key,value) in freq_map.items():
        if value ==k:
            print(key)