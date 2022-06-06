# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_to_sum = {None: 0}
        
        def node_sum(node):
            if node in node_to_sum:
                return node_to_sum[node]
            
            node_to_sum[node] = node.val + node_sum(node.left) + node_sum(node.right)
            return node_to_sum[node]
        

        def dfs(node,prev_total):
            if not node:
                return
            
            right_sum = node_sum(node.right)
            node.val += right_sum + prev_total
            dfs(node.right,prev_total)
            dfs(node.left,node.val)
            

        dfs(root,0)
        return root
        
        