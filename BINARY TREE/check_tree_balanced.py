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


def height(root):
    if root == None: return 0
    return 1+ max (height(root.left),height(root.right))
def isBalanced(root):
    if root == None: return True
    lh=height(root.left)
    rh= height(root.right)
    if lh-rh >1 or rh-lh >1: return False
    isleftbalanced = isBalanced(root.left)
    isrightbalanced = isBalanced(root.right)

    if isleftbalanced and isrightbalanced:
        return True
    else:
        return False

# better function for decrease the time complexity
def getHeightAndCheckBalanced(root):
    if root == None: return 0, True
    lh,isleftbalanced = getHeightAndCheckBalanced(root.left)
    rh,isrightbalanced = getHeightAndCheckBalanced(root.right)
    h=1+max(lh,rh)
    if lh - rh > 1 or rh - lh > 1: return False,h
    if isleftbalanced and isrightbalanced:
        return True,h
    else:
        return h,False




