# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def helper(root):
            if not root:
                return None
            
            if not root.left and not root.right:
                return root
            
            left,right = helper(root.left),helper(root.right)
            
            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
                
            return right if right != None else left
            
            
        helper(root)

                
        