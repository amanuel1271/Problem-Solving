# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxheap = []
        Q = deque([root])
        level = 1
        
        while Q:
            size = len(Q)
            level_sum = 0
            for i in range(size):
                node = Q.popleft()
                level_sum += node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                    
            heapq.heappush(maxheap,(-level_sum,level))
            level += 1
            
        return maxheap[0][1]
            
        
        