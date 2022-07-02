# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxx  = 0
        
        def dfs(node,minn,maxx):
            if not node:
                return 0
            
            self.maxx = max(self.maxx,abs(node.val - minn),abs(node.val - maxx))
            dfs(node.left,min(minn,node.val),max(maxx,node.val))
            dfs(node.right,min(minn,node.val),max(maxx,node.val))
            
            
        dfs(root,root.val,root.val)
        return self.maxx
            
            
        