## IDENTIFY CYCLE LINKED LIST

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def detectCycle(head) :
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False