# two string are anagram if and only if sets have same length and same frequency

# STEPS---> Check on length of both strings
# prepare freq map using dict for both s1 and s2
# also check the the number of uniqye characters using dictionary

# check if actual keys and values are same or not


def check_anagram(s1, s2):
    # check if the length of s1 and s2 is different?
    if len(s1)!=len(s2):
        return False
    d1={}
    for element in s1:
        if element in d1:
            d1[element]=d1[element]+1
        else:
            d1[element]=1

    d2={}
    for element in s2:
        if element in d2:
            d2[element]=d2[element]+1
        else:
            d2[element]=1

    if len(d1.keys())!=len(d2.keys()):
        return False
    for pair in d1.items():
        key=pair[0]
        value=pair[1]
        if key in d2 and d2[key]==value:
            continue
        else:
            return False
    return True
print(check_anagram(input("enter s1 : "), input("enter s2 : ")))