# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        Q = deque([root])
        result = []
        
        while Q:
            queue_len = len(Q)
            maxx = -math.inf
            
            for i in range(queue_len):
                node = Q.popleft()
                maxx = max(maxx,node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
            result.append(maxx)
            
        return result