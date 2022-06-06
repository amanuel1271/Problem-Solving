# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Q = deque([root])
        res = root.val
        
        while Q:
            queue_len = len(Q)
            for i in range(queue_len):
                node = Q.popleft()
                if i == 0:
                    res = node.val
                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)
        

        return res