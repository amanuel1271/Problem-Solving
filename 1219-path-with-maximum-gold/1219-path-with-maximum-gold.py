class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        def dfs(i,j):
            if  i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            maxx,gold = 0,grid[i][j]
            grid[i][j] = 0
            for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                maxx = max(maxx,dfs(x,y) + gold)
                
            grid[i][j] = gold
            return maxx
        
        maxx = 0
        for r in range(m):
            for c in range(n):
                maxx = max(maxx,dfs(r,c))
                    
        return maxx
                
            
                