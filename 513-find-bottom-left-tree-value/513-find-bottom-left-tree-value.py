# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Q = deque([root])
        res = [[root.val]]
        
        while Q:
            size = len(Q)
            row_vals = []
            for i in range(size):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                    row_vals.append(node.left.val)
                if node.right:
                    Q.append(node.right)
                    row_vals.append(node.right.val)
            
            if row_vals != []:
                res.append(row_vals)
        

        return res[-1][0]