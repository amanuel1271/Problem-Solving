# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def helper(self,root):
            if not root:
                return True
            elif not root.left and not root.right:
                self.count += 1
                return True
            
            childrenunil = helper(self,root.left)
            childrenunir  = helper(self,root.right)
            left = (not root.left) or (root.left.val == root.val)
            right = (not root.right) or (root.right.val == root.val)
            
            if (childrenunil and childrenunir) and left and right:
                self.count += 1
                return True
            else:
                return False
        
        helper(self,root)
        return self.count
        
