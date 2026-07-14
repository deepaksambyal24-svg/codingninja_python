import queue


class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def print_treeDetailed(root):
    if root == None:
        return
    print(root.data,end=":")
    if root.left != None:
        print("l-",root.left.data,end=" ")
    if root.right != None:
        print("r-",root.right.data,end=" ")
    print()
    print_treeDetailed(root.left)
    print_treeDetailed(root.right)
import queue as q
def takelevelwiseTreeInput():
    q=queue.Queue()
    print("enter root")
    rootData=int(input())
    if (rootData==-1):
        return  None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print("enter left",current_node.data)
        left_childdata =int(input())
        if left_childdata!=-1:
            left_child = BinaryTreeNode(left_childdata)
            current_node.left = left_child
            q.put(left_child)

        print("enter right", current_node.data)
        right_childdata = int(input())
        if right_childdata != -1:
            right_child = BinaryTreeNode(right_childdata)
            current_node.right = right_child
            q.put(right_child)
    return root
root = takelevelwiseTreeInput()
print_treeDetailed(root)