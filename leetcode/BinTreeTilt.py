# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def sum(root,dic):
            if root in dic:
                return dic[root]
            
            if not root:
                return 0
            elif root and not root.left and not root.right:
                return root.val
            
            dic[root] = root.val + sum(root.left,dic) + sum(root.right,dic)
            return  dic[root]
            
        def helper(root,dic,dic2):
            if not root:
                return 0
            
            root.val = abs(sum(root.left,dic) - sum(root.right,dic))
            helper(root.left,dic,dic2)
            helper(root.right,dic,dic2)
            
            if root in dic2:
                return dic2[root]
            
            dic2[root] = sum(root,dic2)
            return dic2[root]
        
        dp,dp2 = {} ,{} # dictionary to map the node and the sum, to avoid repeated calculations
        return helper(root,dp,dp2)
        
        
            
        
