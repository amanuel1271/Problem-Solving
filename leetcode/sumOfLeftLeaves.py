class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def addleft(root,isleft):
            if not root:
                return 0
            
            count = 0
            
            if not root.left and not root.right and isleft:
                count += root.val
            elif root.left:
                count += addleft(root.left,True)
            if root.right:
                count += addleft(root.right,False)
                
            return count
            
                
        return addleft(root,False)
