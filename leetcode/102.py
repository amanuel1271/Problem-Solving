
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        
        while queue:
            lenn = len(queue)
            res.append([])
            for i in range(lenn):
                froot = queue.pop(0)
                res[-1].append(froot.val)
                
                if froot.left:
                    queue.append(froot.left)
                if froot.right:
                    queue.append(froot.right)
        
        return res
                    
                    
            
        
        
        
