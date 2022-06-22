# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {root: 0,None: -1}
        def dfs(node,parent):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root.left,root)
        dfs(root.right,root)

        max_depth = max(depth.values())

        def answer(node):
            if not node or depth[node] == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)
        
                
                
        
            
        