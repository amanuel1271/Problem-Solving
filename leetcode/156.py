# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            
            if root.left:
                root.left.left = root.right
                root.left.right = root
                if self.ini:
                    self.fnode = root.left
                self.ini = False
                root.left,root.right = None,None
            else:
                if self.ini:
                    self.fnode = root
                root.left,root.right = None,None
                self.ini = False
                    
            
                
            dfs(root.right)
        
        self.fnode = None
        self.ini = True
        dfs(root)
        return self.fnode
            
        
