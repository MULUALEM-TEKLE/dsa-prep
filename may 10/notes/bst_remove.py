def min_node(root) :
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur
 
def remove(root, val): 
    # base condition, reached the end of the leaves
    if not root :
        return None
    # if val is greater than the current root
    if val > root.val : 
        root.right = remove(root.right , val)
        # recursively find and remove the node containing val from the right subtree
        # and return the value to the current root right
    # else if val is less than the current root
    elif val < root.val :
        root.left = remove(root.left , val)
        # recursively find and remove the node containing val from the left subtree
        # and return the value to the current root left

    # else if val is equal to current node's value:
    else : 
      
        # now we've got a match
        # check if the node has a child on either side or on both sides
        # if node has a child on the right side
        if not root.left:
            return root.right
            # return the left child back
        #if the node has child on the left side
        elif not root.right :
            return root.left
            # return the right side back
        # if the node has both left and right child
        else:
            # find the minimum value from the right subtree or the max value from the left subtree
            min_node = min_node(root.right)
            # (this will ensure our tree will stay relatively balanced and correct) 
            # then set the root.val to that minimum node.val
            root.val = min_node.val
            # then recursively find and remove that minimum node from the right or maximum node from the left
            # and assign it back to the right/left of the new root node's right/left side
            root.right = remove(root.right, min_node.val)
    # return node
    return root

