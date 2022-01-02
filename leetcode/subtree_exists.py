class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root1,root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif not root1.left and not root1.right and not root2.left and not root2.right:
                return root1.val == root2.val
            
            return root1.val == root2.val and same(root1.left,root2.left) and same(root2.right,root1.right)
        
        def helper(root):
            mid,left,right = False,False,False
            
            if root.val == subRoot.val:
                mid = same(root,subRoot)
                if mid:
                    return True
            
            if root.left:
                left = helper(root.left)
                if left:
                    return True
                
            if root.right:
                right = helper(root.right)
                if right:
                    return True
            
            return False
        
        return helper(root)
        
