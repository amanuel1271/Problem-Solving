# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:  
                
        def traverse(node):
            if not node:
                return None
            
            if node.val < low:
                return traverse(node.right)
            elif node.val > high:
                return traverse(node.left)
            
            if node.val == low:
                node.left = None
            if node.val == high:
                node.right = None
                
            if node.left:
                node.left = traverse(node.left)
            if node.right:
                node.right = traverse(node.right)
                
            return node
                

        return traverse(root)
        