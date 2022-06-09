# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        #### restructure root
        def restructure(node):
            while node and not (low <= node.val <= high):
                if node.val < low:
                    node = node.right
                else:
                    node = node.left  
                    
            if node and node.val == low:
                node.left = None
            elif node and node.val == high:
                node.right = None
                
            return node
            
                
        def traverse(node):
            if not node:
                return
            
            if node.left:
                node.left = restructure(node.left)
                traverse(node.left)
            if node.right:
                node.right = restructure(node.right)
                traverse(node.right)
                
                
        root = restructure(root)
        traverse(root)
        return root
        