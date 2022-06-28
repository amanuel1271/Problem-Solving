# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def count_from_children(child,node):
            cnt = 0
            if child:
                if child.val > 1:
                    cnt += child.val -1
                    node.val += child.val - 1
                elif child.val <= 0:
                    cnt += 1 - child.val
                    node.val -= 1 - child.val      
            return cnt
                
        def dfs(node):
            if not node:
                return 0
            
            count = 0
            count += dfs(node.left)
            count += count_from_children(node.left,node)
            count += dfs(node.right)
            count += count_from_children(node.right,node)
            
            return count
        
        return dfs(root)
            
        