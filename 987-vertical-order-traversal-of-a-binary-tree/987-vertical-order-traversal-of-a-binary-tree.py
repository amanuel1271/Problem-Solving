# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        minheap = []
        
        def bfs():
            x,y = 0,0
            Q = deque([(x,y,root)])
            minheap.append((x,y,root.val))
            
            while Q:
                size = len(Q)
                for _ in range(size):
                    c,r,node = Q.popleft()
                    if node.left:
                        Q.append((c-1,r+1,node.left))
                        minheap.append((c-1,r+1,node.left.val))
                    if node.right:
                        Q.append((c+1,r+1,node.right))
                        minheap.append((c+1,r+1,node.right.val))
                        
        bfs()
        heapify(minheap)
        ans = []
        prev_col = -math.inf
        
        while minheap:
            c,r,val = heappop(minheap)
            if c != prev_col:
                ans.append([val])
                prev_col = c
            else:
                ans[-1].append(val)
        
        return ans
                
                    
                    
            
            
        