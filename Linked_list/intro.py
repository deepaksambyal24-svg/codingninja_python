# arrays uses continous  memory allocation for creation
# if we want to create an array of large than the contineous available block it through an error
# so linked lists are space optimized version of arrays
# so linked lists are chain like structure and of non continuous fashion
# nodes are connected by links data is stored in nodes
#node is actual object that create in memory , so memory blocks are the nodes


class Node():
    def __init__(self, value):
        self.data = value       # storing the incoming value passed by user in the data properties
        self.next = None        # intially the memory address is node and it is the memory address of next node
# nodes are nothing but are object

n1=Node(1)
n2=Node(2)
n3=Node(3)
print(n1.data)
print(n2)       # it gives memory reference of the  node

print(n1.data,n1.next)      # properties of node
print(n2.data,n2.next)
# these above nodes are indipendent because are intially none
n1.next=n2
print(n1.next)

n2.next=n3
print(n2.next)          # it gives the memory address of next node
