# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:  
                
        def BstTrim(node):
            if not node:
                return None
            
            if node.val < low:
                return BstTrim(node.right)
            elif node.val > high:
                return BstTrim(node.left)
            
            node.left = None if node.val == low else BstTrim(node.left)
            node.right = None if node.val == high else BstTrim(node.right) 
            return node
                
        return BstTrim(root)
        