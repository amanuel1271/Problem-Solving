# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values_inorder = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            values_inorder.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        def make_balanced(lst):
            if len(lst) == 0:
                return None 
            
            mid = len(lst) // 2
            
            root = TreeNode(lst[mid])
            root.left = make_balanced(lst[:mid])
            root.right = make_balanced(lst[mid+1:])
            
            return root
        
        return make_balanced(values_inorder)