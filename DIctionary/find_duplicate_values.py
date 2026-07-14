def duplicate_character(inp):
    freq_map={} # to store key values
    for i in range (0,len(inp)):
        if inp[i] in freq_map:
            freq_map[inp[i]]+=1
        else:
            freq_map[inp[i]]=1
    for (key,value) in freq_map.items():
        if value>1:
           print(key)


    # lets prepare this whole freq mappling
