# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

```
BFS traversal fot right side view
```
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        res = []
        queue = []
        queue.append(root)
        
        while queue:
            lenn = len(queue)
            temp = None
            for i in range(lenn):
                froot = queue.pop(0)
                temp = froot.val
                if froot.left:
                    queue.append(froot.left)
                if froot.right:
                    queue.append(froot.right)
            res.append(temp)
        return res
            
                    
                
        
            
            
