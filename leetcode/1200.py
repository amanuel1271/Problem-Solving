class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(root,lst):
            if not root:
                return 
            
            lst.append(root.val)
            helper(root.left,lst)
            helper(root.right,lst)
            
        acc = []
        helper(root,acc)
        acc.sort()
        
        minn = float(inf)
        for i in range(len(acc) - 1):
            minn = min(minn,abs(acc[i] - acc[i+1]))
            
        return int(minn)
