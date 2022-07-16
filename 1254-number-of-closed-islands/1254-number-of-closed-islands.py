class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        cnt = 0
        
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            elif grid[i][j] == 1:
                return True
            
            grid[i][j] = 1
            l,r,u,b = dfs(i,j-1),dfs(i,j+1),dfs(i-1,j),dfs(i+1,j)
            
            return l and r and u and b
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if dfs(r,c):
                        cnt += 1
                        
        return cnt
        
        