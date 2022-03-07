# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root,target,acc):
            if not root.left and not root.right:
                return (acc + root.val == target)
            
            left,right = False,False
            if root.left:
                left = helper(root.left,target,acc + root.val)
            if root.right:
                right = helper(root.right,target,acc + root.val)
                
            return left or right
            
            
            
        if not root:
            return False
        return helper(root,targetSum,0)
        