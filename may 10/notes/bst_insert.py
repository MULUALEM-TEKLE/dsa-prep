class TreeNode : 
    def __init__(self, val ):
        self.val = val 
        self.left = self.right = None

def insert(root, val):
    if not root : 
        return TreeNode(val)
    
    if val > root.val : 
        root.right = insert(root.right, val)
    elif val < root.val : 
        root.left = insert(root.left, val)
        
    return root