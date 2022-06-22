# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {root: 0,None: -1}
        self.maxdepth = 0
        
        def dfs(node,parent):
            if node:
                depth[node] = depth[parent] + 1
                self.maxdepth = max(self.maxdepth,depth[node])
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root.left,root)
        dfs(root.right,root)

        def answer(node):
            if not node:
                return None
            elif depth[node] == self.maxdepth:
                return node
            
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)
        
                
                
        
            
        