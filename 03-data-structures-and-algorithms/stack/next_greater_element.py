def is_empty(st):
    return len(st) == 0

def next_greater(arr):
    n = len(arr)
    output=[-1]*n  # n length array all intialised by -1
    st=[] #stack of indexes

    st.append(0)
    for i in range(1,n):
        while not is_empty(st) and arr[st[i]]>arr[st[i-1]]:
            #we got the answer
            output[st[len(st)-1]] =arr[i]
            st.pop()
            st.append(i)
    return output
