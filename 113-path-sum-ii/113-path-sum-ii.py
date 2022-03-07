# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root,acclst):
            if not root:
                return
            elif not root.left and not root.right:
                acclst = acclst + [root.val]
                if sum(acclst) == targetSum:
                    self.res = [acclst] + self.res
                return
            
            
            helper(root.left,acclst + [root.val])
            helper(root.right,acclst + [root.val])
            
        self.res = []
        helper(root,[])
        return self.res
        