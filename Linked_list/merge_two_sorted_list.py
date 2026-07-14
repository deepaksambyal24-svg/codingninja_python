from multiprocessing import dummy


def merge_sorted_lists(head1,head2) :
    newhead=Node(-1)
    dummmy=newhead
    i=head1
    j=head2
    while i is not None and j is not None :
        if i.data<j.data :
            dummy.next=i
            i=i.next

        else:
            dummy.next=j
            j=j.next

        dummy.next.next=None
        dummy=dummy.next
        ## may be l1 exhausted
        if j is not None :
            dummy.next=j
        ## may be l2 exhausted
        if i is not None :
            dummy.next=i
        result= newhead.next
        #newhead.next = NONE
        RETURN=result
        