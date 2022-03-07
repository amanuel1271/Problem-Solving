# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,acc):
            if not root:
                return 0
            if not root.left and not root.right:
                return (acc * 10) + root.val
            

            return helper(root.left,(acc * 10) + root.val) + helper(root.right,(acc * 10) + root.val)
        
        
        return helper(root,0)
    

            
        