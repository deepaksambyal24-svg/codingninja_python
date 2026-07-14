class Node:
        def __init__(self,value):
            self.value=value # storing the incoming value passed by user in the data property
            self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_at_head(self,value):
        new=Node(value)    # new node created
        new.next=self.head      # connect the new node with old head
        self.head=new           # update the head of LL with the new node

    def remove_from_head(self):
        if self.head==None:
            return
        newHead=self.head.next
        self.head.next=None
        self.head=newHead

    def is_empty(self):
        return self.head==None

    def get_head(self):
        if self.head==None:
            return
        return self.head.data

class Stack:
    def __init__(self):
        self.__ll=LinkedList()     # initialise a brand new empty ll

    def push(self,data):
        self.__ll.add_at_head(data)

    def pop(self):
        if self.__ll.is_empty():
            print("Stack is empty")
            return
        self.__ll.remove_from_head()

    def peek(self):
        if self.__ll.is_empty():
            print("Stack is empty")
            return
        return self.__ll.get_head().value