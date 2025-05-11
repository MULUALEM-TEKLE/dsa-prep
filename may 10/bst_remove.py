def min_node(root) :
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur
 