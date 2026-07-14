# to delete the head node
# 1. keep track of new head : new head = self.head.next
# break connection : self.head.next = None
# self.head = new head
# to find the tail
# we have to traverse to whole list
#and the condition for tail is temp.next=None
from Linked_list.head_linked_list import LinkedList


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
        def insert_tail(self,data):
            # check if linklist is empty
            if self.head==None:
                self.insert_at_head(data)
                return
            # if ll is not empty
            # find the tail
            temp = self.head
            while(temp.next!=None):
                temp=temp.next
            #once the loop ends temp points t tail
            new =Node(data)
            temp.next=new

ll =LinkedList()
ll.insert_tail(5)
print(ll.head.data)
ll.insert_tail(25)
print(ll.head.data)
print(ll.head.next.data)

def  insert_in_between(self,value,pos):
    if self.head==None:
        self.insert_at_head(value)
        return
    temp = self.head
    while temp.next != None and i < pos:
        temp=temp.next
        i=i+1
    new =Node(value)
    remaining =temp.next
    temp.next=new
    new.next = remaining


ll=LinkedList()
ll.insert_tail(10)
print(ll.head.data)
print(ll.head.next.data)
ll.insert_tail(20)
print(ll.head.data)
print(ll.head.next.data)
ll.insert_in_between(100,1)
print(ll.head.data)
print(ll.head.next.data)

def delete_at_head(self):
    if self.head==None:
        return
    newHead = self.head.next
    self.head.next=None
    self.head=newHead


def delete_at_tail(self):
# prev.next =None
# to access the previous node next.next.next = None
    if self.head == None:
        return
    if self.head.next == None:
        self.head=None
        return
    prev=self.head
    while prev.next.next!=None:
        prev=prev.next
    prev.next = None        # delete between conn between second last and tail



def display(self):
    temp=self.head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next

def count_nodes(self):
    count=0
    temp=self.head
    while temp!=None:
        count+=1
        temp=temp.next
    return count

# for fast iteraton and get mid note
# rabit fast and slow approach
# slow moves one step and fast moves two steps
def mid_node(self):
    slow=self.head
    fast=self.head
    while fast.next!=None and fast.next.next!=None:
        fast=fast.next.next
        slow=slow.next
    return slow
def reverse(self):
    prev=None
    curr=self.head
    while curr!=None:
        remaining=curr.next     # access to remaining list
        curr.next=prev      # reverse the next  ref
        prev=curr           #prepare prev for next iteration
        curr=remaining      # prepare curr for next iteration
    self.head=prev          # update new head

 