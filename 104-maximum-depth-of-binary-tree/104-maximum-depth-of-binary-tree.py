# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root,num):
            if not root.left and not root.right:
                return num
            
            left,right = 0,0

            if root.right:
                right = helper(root.right,num + 1)
            if root.left:
                left = helper(root.left,num + 1)
                
            return max(left,right)
        
        if not root:
            return 0
        return helper(root,1)
        