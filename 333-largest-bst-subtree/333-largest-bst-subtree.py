# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def isBST(node,minn,maxx):
            if not node:
                return True
            
            if node.val >= maxx or node.val <= minn:
                return False
            
            return isBST(node.left,minn,node.val) and isBST(node.right,node.val,maxx)
        
        @lru_cache(None)
        def countNodes(node):
            if not node:
                return 0
            return 1 + countNodes(node.left) + countNodes(node.right)
            
            
        
        
        def helper(node):
            if not node:
                return 0
            
            if isBST(node,-math.inf,math.inf):
                return countNodes(node)
            
            return max(helper(node.left),helper(node.right))
        
        return helper(root)
                
        