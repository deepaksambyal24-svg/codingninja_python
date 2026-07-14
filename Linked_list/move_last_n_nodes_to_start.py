
def moveLastNNodesToStart(head,n):
    if head == None or n ==0:
        return head         # ll is empty or dont move anything
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
    while fast != None:
        fast = fast.next
        slow = slow.next
    new_head = slow.next
    slow.next = None            # breaking the connection
    fast.next=head
    head = new_head             # update the new_head as head of the list
    return head

ll.head