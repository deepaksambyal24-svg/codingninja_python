def anagram(s1,s2):
    if len(s1)!=len(S2):
        return False
    d1={}
    for char in s1:
        if char in d1:
            d1[char]+=1
        else:
            d1[char]=1
    d2={}
    for ele in s2:
        if ele in d2:
            d2[ele]+=1
        else:
            d2[ele]=1
   #check the number of uniques keys are same or not
    if (len(d1.keys)) != len(d2.keys):
        return False
    for pair in d1.items():
        key =pair[0]
        value =pair[1]
        if key in d2 and d2[key]==value:
            continue
        else:
            return False
    return True

