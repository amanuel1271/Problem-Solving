# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        
        if not root:
            return root
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
                    
        for i in range(len(res)):
            if i % 2 != 0:
                res[i] = res[i][::-1]
        return res
    
                    
        