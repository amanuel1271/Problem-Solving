# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,acc):
            if not root:
                return acc
            return  helper(root.right,helper(root.left,acc)) + [root.val]
        
        return helper(root,[]) if root else []