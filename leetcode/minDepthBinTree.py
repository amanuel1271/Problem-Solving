class Solution: 
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + self.minDepth(root.right)
