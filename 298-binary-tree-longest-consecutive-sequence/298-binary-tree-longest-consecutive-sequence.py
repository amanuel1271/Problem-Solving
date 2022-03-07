# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def helper(root,precons,preval):
            if not root:
                return
            
            if preval != math.inf and root.val == preval + 1:
                consval = precons + 1 #update by 1
                self.maxx = max(self.maxx,consval)
            else:
                consval = 1 #reset
            
            helper(root.left,consval,root.val)
            helper(root.right,consval,root.val)
        
        self.maxx = 1
        helper(root,1,math.inf)
        return self.maxx
            
            
            
            
            
            

            
            
                
                
        