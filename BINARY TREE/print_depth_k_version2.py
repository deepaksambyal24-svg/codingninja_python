def printDepthkv2(root,k,d=0):
    if root == None:
        return
    if k ==d:
        print(root.data)
        return
    printDepthkv2(root.left,k,d+1)
    printDepthkv2(root.right,k,d+1)