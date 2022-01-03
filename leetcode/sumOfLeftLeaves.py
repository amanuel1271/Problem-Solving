class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def addleft(root,isleft):
            if not root:
                return 0
                
            return root.val + addleft(root.left,True) + addleft(root.right,False)
            
                
        return addleft(root,False)
