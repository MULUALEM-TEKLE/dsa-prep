""" 
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []

        res = []
        q = deque([root])

        while len(q) : 
            tmp = []
            for _ in range(len(q)) : 
                node = q.popleft()
                tmp.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            res.append(tmp)

        res.reverse()
        return res