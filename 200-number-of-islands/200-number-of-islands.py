

class Solution:
    def numIslands(self, grid):
        m,n = len(grid),len(grid[0])
        visited = set()
        count = 0
        
        def dfs(i,j):
            if (i,j) in visited or i < 0 or i > m-1 or j < 0 or j > n-1 or grid[i][j] == '0':
                return
            
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
                
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
                    
        return count
                    
                
        
        