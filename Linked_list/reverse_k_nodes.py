def reverseKNodes(head, k):
    prev = None
    cur = head
    count = 0
    next = None
    while cur  is not None and  count < k:
        next = cur.next
        cur.next = prev
        prev = cur
        count = count + 1
        cur = next
    return prev