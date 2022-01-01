# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def helper(self,croot):
            if not croot:
                return

            # check whether it is better to compare the left tree or right
            store_min = self.min
            self.min = min(abs(croot.val - target),self.min)
            if self.min != store_min:
                self.sign = True if croot.val >= target else False

            if croot.val >= target:
                helper(self,croot.left)
            elif croot.val < target:
                helper(self,croot.right)

            return
        
        self.min = float('inf')
        self.sign = True
        helper(self,root)
        return int(self.min + target) if self.sign else int(target - self.min)
        
