# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:  
                
        def trim_(node):
            if not node:
                return None
            
            if node.val < low:
                return trim_(node.right)
            elif node.val > high:
                return trim_(node.left)
            
            if node.val == low:
                node.left = None
            else:
                node.left = trim_(node.left)
            if node.val == high:
                node.right = None
            else:
                node.right = trim_(node.right)
                
                
            return node
                

        return trim_(root)
        