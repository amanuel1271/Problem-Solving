class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        queue = deque([])
        max_color = 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((1,r,c))
        
        while queue:
            color,cur_x,cur_y = queue.popleft()
            max_color = max(max_color,color)
            
            for x,y in [(cur_x+1,cur_y),(cur_x,cur_y+1),(cur_x-1,cur_y),(cur_x,cur_y-1)]:
                if 0 <=x<m and 0<=y<n and grid[x][y] == 0:
                    grid[x][y] = color + 1
                    queue.append((color+1,x,y))
                    
                    
                    
        return -1 if max_color == 1 else max_color - 1
                    
            
            
        