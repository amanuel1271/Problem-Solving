# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:  
                
        def bstTrim(node):
            if not node:
                return None
            
            if node.val < low:
                return bstTrim(node.right)
            elif node.val > high:
                return bstTrim(node.left)
            
            node.left = None if node.val == low else bstTrim(node.left)
            node.right = None if node.val == high else bstTrim(node.right) 
            return node
                
        return bstTrim(root)
        