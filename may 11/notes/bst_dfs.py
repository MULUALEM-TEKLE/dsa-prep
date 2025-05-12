def traverse_inorder(root) : 
    if not root :
        return
    traverse_inorder(root.left)
    print(root.val)
    traverse_inorder(root.right)
   

def traverse_inorder_reverse(root) : 
    if not root :
        return
    traverse_inorder(root.right)
    print(root.val)
    traverse_inorder(root.left)


def traverse_preorder(root):
    if not root :
        return
    print(root.val)
    traverse_inorder(root.left)
    traverse_inorder(root.right)

def traverse_postorder(root):
    if not root :
        return
    traverse_inorder(root.left)
    traverse_inorder(root.right)
    print(root.val)