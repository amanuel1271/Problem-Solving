class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def addleft(root,isleft):
            if not root:
                return 0
           
                
            return  (root.val if isleft else 0) + addleft(root.left,True) + addleft(root.right,False)
            
                
        return addleft(root,False)
