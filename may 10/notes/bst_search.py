def search(root , target):
    if not root : 
        return -1

    if target < root.val : 
        return search(root.left , target)
    elif target > root.val:
        return search(root.right , target)
    else :
        return root.val