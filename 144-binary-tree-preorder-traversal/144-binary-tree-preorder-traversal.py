# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,acc):
            if not root:
                return acc
    
            acc.append(root.val)
            acc2 = helper(root.left,acc)
            return helper(root.right,acc2)
        
            
            
        return helper(root,[]) if root else []
        