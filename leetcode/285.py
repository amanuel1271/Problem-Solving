class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        def dfs(root):
            left,right = None,None
            if root and not root.right and not root.left:
                return root
            
            if root.left:
                left = dfs(root.left)
                
            if left and left is p:
                self.store = root
            
        
            if root.right:   
                nextt = root.right
                while nextt.left:
                    nextt = nextt.left
                
                if root is p:
                    self.store = nextt
                    
                
                right = dfs(root.right)
            
            return root if not right else right

            
        self.store = None
        dfs(root)
        return self.store
            
        
