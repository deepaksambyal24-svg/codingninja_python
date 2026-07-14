import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(lst):
    def build(start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        root = BinaryTreeNode(lst[mid])

        root.left = build(start, mid - 1)
        root.right = build(mid + 1, end)

        return root

    return build(0, len(lst) - 1)


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
if (n > 0):
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst)
preOrder(root)