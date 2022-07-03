class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        count = 0
        
        @lru_cache(None)
        def dfs(i,j):
            ans = 1
            for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    ans += dfs(x,y)
            return ans
            

        for i in range(m):
            for j in range(n):
                count += dfs(i,j)
                    
        return count%(10**9+7)
                    
        