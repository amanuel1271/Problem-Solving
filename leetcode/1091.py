class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        minn = math.inf ## holds the minimum value
        visit = set()
        visit.add((n-1,n-1))
        Q = deque([(n-1,n-1,1,visit)])
        
        while Q:
            x,y,step,visited = Q.popleft()
    
            if x == 0 and y == 0:
                minn = min(step,minn)
            
            eight_dir = [(x-1,y),(x+1,y),(x,y-1),(x,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
            
            for (xl,yl) in eight_dir:
                if 0 <= xl < n and 0 <= yl < n and (xl,yl) not in visited and grid[xl][yl] == 0:
                    visited.add((xl,yl))
                    Q.append((xl,yl,step + 1,visited))
            
            
        return minn if minn != math.inf else -1
