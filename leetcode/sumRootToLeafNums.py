# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rootToLeaf(root,val):
            if not root:
                return 0
            elif not root.left and not root.right:
                return val
    
            left_val,right_val = 0,0
        
            if root.left:
                left_val = int(str(val) + str(root.left.val))

            if root.right:
                right_val = int(str(val) + str(root.right.val))

            
            return rootToLeaf(root.left,left_val) + rootToLeaf(root.right,right_val)         
            
            
        return rootToLeaf(root,root.val)
    
        
