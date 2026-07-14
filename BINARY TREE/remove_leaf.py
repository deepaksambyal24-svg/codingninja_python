#base case if root == None,
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
# ask the user for root data
def treeInput():
    rootData=int(input())
    if rootData == -1: return None
    leftTree=BinaryTreeNode(rootData)
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root
def numNodes(root):
    if root == None: return 0
    leftCount=numNodes(root.left)
    rightCount=numNodes(root.right)
    return 1+leftCount+rightCount

def removeLeaf(root):
    if root == None: return None
    if root.left == None and root.right == None: return None
    root.left=removeLeaf(root.left)
    root.right=removeLeaf(root.right)
    return root
root = treeInput()
print_treeDetailed(root)
root = removeLeaf(root)
print("new tree is :")
print_treeDetailed(root)




