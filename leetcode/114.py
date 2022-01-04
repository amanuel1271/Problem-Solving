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
        
        
        
