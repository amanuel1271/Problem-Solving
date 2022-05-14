# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
            ret = []
            
            def dfs(node):
                if not node:
                    return 0
                
                depth = max(dfs(node.left),dfs(node.right))+1
                
                if len(ret) < depth:
                    ret.append([])
                    
                ret[depth-1].append(node.val)
                return depth
            
            dfs(root)
            return ret
        