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

def buildTreeFromPreorder(pre,inorder):
    if len(pre)==0:
        return None
    rootData=pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInorder=-1
    for i in range (0,len(inorder)):
        if inorder[i] == rootData:
            rootIndexInorder=i
            break  ## this will give me index of root order

    if rootIndexInorder==-1:
        return None
    leftInOrder=inorder[0:rootIndexInorder]
    rightInOrder=inorder[rootIndexInorder+1:]

    lenLeftSubTree=len(leftInOrder)
    leftPreorder=pre[1:lenLeftSubTree+1]
    rightPreorder=pre[lenLeftSubTree+1:]

# use recursion to build left and right subtree
    leftChild = buildTreeFromPreorder(leftPreorder,leftInOrder)
    rightChild = buildTreeFromPreorder(rightPreorder,rightInOrder)
    root.left=leftChild
    root.right=rightChild
    return root