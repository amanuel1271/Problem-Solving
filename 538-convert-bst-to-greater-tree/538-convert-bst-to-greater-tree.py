# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node,prev_total):  # has to return the sum so far
            if not node:
                return 0
            
            right_sum = dfs(node.right,prev_total)
            val = node.val
            node.val += right_sum + prev_total
            return val + right_sum + dfs(node.left,node.val)
            
        dfs(root,0)
        return root
        
        