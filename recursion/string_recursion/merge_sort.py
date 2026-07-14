def merge(a1, a2, a):        # merge a1 and a2 into a new list "a"
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:      # element of a1 is smaller
            a[k] = a1[i]

            i = i + 1
            k = k + 1
        else:                  # element of a2 is smaller
            a[k] = a2[j]
            j = j + 1
            k = k + 1

    # remaining elements of a1
    while i < len(a1):

        a[k] = a1[i]

        i = i + 1
        k = k + 1
    # remaining elements of a2
    while j < len(a2):

        a[k] = a2[j]

        j = j + 1
        k = k + 1
def mergeSort(a):
    # BASE CASE
    # stop recursion when only one or zero elements remain
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a) // 2
    a1 = a[0:mid]      # left half
    a2 = a[mid:]       # right half
    # recursive sorting
    mergeSort(a1)
    mergeSort(a2)
    # merge sorted halves
    merge(a1, a2, a)




a = [2,13,4,1,3,6,28]

mergeSort(a)

print(a)