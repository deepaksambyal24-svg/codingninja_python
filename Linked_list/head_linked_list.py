# add at head that means :- create a node ,step 2 connect the node with link list
# next of our node refer the memory address of old head
# update the head variable to new node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
        def __init__(self):
            self.head=None
        def insert_at_head(self,data):
            # create a brand new node
            new_node=Node(data)
            #connect the node with existing head
            new_node.next=self.head
            #update the head
            self.head=new_node

ll=LinkedList()
ll.insert_at_head(5)
print(ll.head.data)
ll.insert_at_head(4)
print(ll.head.data)
ll.insert_at_head(3)
print(ll.head.data)