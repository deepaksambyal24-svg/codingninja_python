
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def detectCycle_start(head) :
    slow = head
    fast = head
    collision_node = None
    while fast is not None and slow is not  None and  fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            collision_node = slow
            break

    i=head
    j=collision_node
    while i!=j:
        i=i.next
        j=j.next
    return i

    return False