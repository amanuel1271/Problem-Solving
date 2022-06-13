class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        @lru_cache(None)
        def dfs(i,j):
            if i == m-1:
                return grid[i][j]
            
            minn = math.inf
            for col in range(n):
                minn = min(minn,grid[i][j] + dfs(i+1,col) + moveCost[grid[i][j]][col])
                
            return minn
        
        minn = math.inf
        for col in range(n):
            minn = min(minn,dfs(0,col))
        return minn