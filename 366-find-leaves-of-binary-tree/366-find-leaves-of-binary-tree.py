# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs_leaf(node):
            if not node:
                return False
            elif not node.left and not node.right:
                return True
            
            if dfs_leaf(node.left):
                res[-1].append(node.left.val)
                node.left = None
            if dfs_leaf(node.right):
                res[-1].append(node.right.val)
                node.right = None
    
            return False
        
             
        while root.left or root.right:
            res.append([])
            dfs_leaf(root)
            
        res.append([root.val])
        return res
            