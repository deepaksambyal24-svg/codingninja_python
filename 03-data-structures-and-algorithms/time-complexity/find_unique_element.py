#unique element by using XOR
def find_unique_element(arr,n):
    ans=0
    for el in arr:
        ans =ans ^el
    return ans