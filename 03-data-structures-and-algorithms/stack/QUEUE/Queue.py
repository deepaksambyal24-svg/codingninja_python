from Stack.QUEUE.INTRO import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_at_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            #if the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node       # connecting old tail with the new node
            self.tail = new_node            # se are updating tail pointer to point to the new tail
    def remove_at_head(self):
        if self.head == None:
        # if ll is empty
            return
        if self.head.next == None:
            # ll is only having one element
            self.head = None
            self.tail = None
            return
        newHead = self.head.next
        self.head.next = None
        self.head = newHead
    def is_empty(self):
        return self.head == None
    def get_head(self):
        if self.is_empty():
            return
        return self.head.value

class Queue:
    def __init__(self):
        self.ll = LinkedList()
    def enqueue(self, value):
        self.ll.add_at_tail(value)
    def dequeue(self):
        if self.ll.is_empty():
            print('Queue is empty')
            return
        self.ll.remove_at_head()
    def front(self):
        if self.ll.is_empty():
            print('Queue is empty')
            return
        return self.ll.head.value

    qu=Queue()
    qu.enqueue(10)
    qu.enqueue(20)
    qu.enqueue(30)
    qu.dequeue()
    qu.front()