# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def init(self):
            self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':      
        def recurse(curroot):
            if not curroot:
                return False
            
            left = recurse(curroot.left)
            right = recurse(curroot.right)
            
            mid = curroot.val == p.val or curroot.val == q.val
            
            if mid + left + right == 2:
                self.ans = curroot
            
            return mid or left or right
        
        recurse(root)
        return self.ans
        