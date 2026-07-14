def is_sorted(a,si):
    l = len(a)
    if si ==l-1 or si ==1:
        return True
    if a[si]>a[si+1]:
        return False
    is_smaller_part_sorted=is_sorted(a,si+1)
    return is_smaller_part_sorted