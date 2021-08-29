# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rearrange(self,root):
        if not root.left and not root.right:
            return root,root # head and tail pointers
        
        if root.left:
            left_head,left_tail = self.rearrange(root.left)
            if root.right:
                right_head,right_tail =  self.rearrange(root.right)
                root.right = left_head
                left_tail.right = right_head
                root.left = None
            else:
                root.right = left_head
                root.left = None
                right_tail = left_tail
                
        else:
            if root.right:
                right_head,right_tail =  self.rearrange(root.right) 
                
        if root.right:
            return root,right_tail
        
        return root,right_tail
            
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.rearrange(root)
        
        
        
