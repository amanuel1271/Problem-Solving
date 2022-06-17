# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(node):
            if not node.left and val < node.val:
                node.left = TreeNode(val)
            elif not node.right and val > node.val:
                node.right = TreeNode(val)
            elif val < node.val:
                insert(node.left)
            else:
                insert(node.right)
                
        if not root:
            return TreeNode(val)
        
        insert(root)
        return root
                
        