
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# all tree would have printed with recursion

def print_tree(root):       # this function only prints the data
    if root == None:        # base case
        return
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)
btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)
btn4 = BinaryTreeNode(4)
btn5 = BinaryTreeNode(5)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
def print_tree_detail(root):       # this function structure of tree
    if root == None:        # base case
        return
    print(root.data,end=":")
    if root.left != None:
        print("L-",root.left.data,end=',')
    if root.right != None:
        print("R-",root.right.data,end='')
    print()
    print_tree_detail(root.left)
    print_tree_detail(root.right)
print_tree_detail(btn1)
