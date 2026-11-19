# if a[md] >= target
# ans =mid
#end=mid+1
#else start = mid +1
def lowerBound(arr: [int], n: int, x: int) -> int:
    start = 0
    end = n - 1

    ans = n

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] >= x:
            ans = mid
            end = mid - 1

        else:
            start = mid + 1

    return ans

