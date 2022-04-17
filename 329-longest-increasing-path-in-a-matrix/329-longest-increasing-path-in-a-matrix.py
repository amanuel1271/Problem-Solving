class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = 1
        
        
        @lru_cache(None)
        def dfs(i,j):
            max_ = 1
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_ = max(max_,dfs(x,y) + 1)
                    
            return max_
            
                        
                
        for x in range(m):
            for y in range(n):
                ans = max(ans,dfs(x,y))
                
        return ans
                
                
        
        
        