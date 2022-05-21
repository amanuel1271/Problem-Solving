# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        
        def check(node,target):
            if not node:
                return
            
            if node.val == target:
                self.count += 1
                
            check(node.left,target-node.val)
            check(node.right,target-node.val)
            
        
        def sumup(node,target):
            if not node:
                return
            
            check(node,target)
            sumup(node.left,target)
            sumup(node.right,target)
        
        sumup(root,targetSum)
        return self.count