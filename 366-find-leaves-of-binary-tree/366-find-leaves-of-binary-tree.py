# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
            ret = []
            self.ret_size = 0
            def dfs(node):
                if not node:
                    return 0
                
                height = max(dfs(node.left),dfs(node.right))+1
                
                if self.ret_size < height:
                    ret.append([])
                    self.ret_size += 1
                    
                ret[height-1].append(node.val)
                return height
            
            dfs(root)
            return ret
        