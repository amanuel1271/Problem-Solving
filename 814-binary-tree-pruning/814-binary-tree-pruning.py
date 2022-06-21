# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def not_contains(node):
            if not node:
                return True
            elif node.val == 1:
                return False
            return not_contains(node.left) and not_contains(node.right)
                
        
        def helper(node):
            if not node:
                return
            
            if node.left and node.left.val == 0:
                if (not_contains(node.left)):
                    node.left = None
                    
            if node.right and node.right.val == 0:
                 if (not_contains(node.right)):
                    node.right = None
                
            helper(node.left)
            helper(node.right)
        
        
        
        
        dummy = TreeNode(1,root)
        helper(dummy)
        return dummy.left
        
        