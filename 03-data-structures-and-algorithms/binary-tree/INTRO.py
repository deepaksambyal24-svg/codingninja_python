# IT HAS  ROOT , AND INSIDE IT WE HAVE DIRECOTRY OR FILES
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)
print(btn1.data)
print(btn1.left)
print(btn1.right)
btn1.left = btn2        # left and right child
btn1.right = btn3