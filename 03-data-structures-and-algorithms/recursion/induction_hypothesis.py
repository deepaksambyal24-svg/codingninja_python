def sum_n(n):
    if n == 0:
        return 0
    small_output= sum_n(n-1)            #this is out hypothesis  we need to prove
    return small_output+n  # if smalloutputiscorrect my output willbe correct
