class Solution:
    def numIslands(self, grid):
#  using bfs and queue 
        s = {(i,j) for i,row in enumerate(grid) for j, col in enumerate(row) if col == '1'}
        num = 0
               
        while s:
            num += 1
            queue = deque([s.pop()])
            while queue:
                i, j = queue.popleft()
                for item in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if item in s:
                        s.remove(item)
                        queue.append(item)
        return num

class Solution:
    def numIslands(self, grid):
        #  attempt using stack and dfs
        s = {(i,j) for i,row in enumerate(grid) for j, col in enumerate(row) if col == '1'}
        num = 0 
        
        while s:
            num += 1
            x,y = s.pop()
            stack = deque([(x,y)])
            
            while stack:
                x,y = stack[-1]
                if (x + 1,y) not in s and (x - 1,y) not in s and (x,y + 1) not in s and (x,y - 1) not in s:
                    stack.pop()
                for nei in [(x - 1,y),(x + 1,y), (x, y - 1), (x, y + 1)]:
                    if nei in s:
                        stack.append(nei)
                        s.remove(nei)
                        break
                        
        return num
                
                
                    
                
