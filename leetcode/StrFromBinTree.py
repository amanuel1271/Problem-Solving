# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(root,acc):
            if not root:
                return acc
            elif root and not root.left and not root.right:
                return acc + str(root.val)
            

            acc = helper(root.left,acc + str(root.val) +  '(') + ')'
            if root.right:
                acc = helper(root.right,acc + '(') + ')'


            return acc
        
        return helper(root,'')
        
