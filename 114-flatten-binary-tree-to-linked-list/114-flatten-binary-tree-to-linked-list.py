# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def helper(root):
            if not root:
                return root
            elif not root.left and not root.right:
                return root
            

            left,right = helper(root.left),helper(root.right)
            if not left:
                root.right = right
                return root
            
            save_left = left
            while save_left.right:
                save_left = save_left.right
                
            save_left.right = right
            root.right = left
            root.left = None
            return root
            
        

        helper(root)

                
        