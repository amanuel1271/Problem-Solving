class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        maxsq = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1],dp[i][j],dp[i+1][j]) + 1
                    maxsq = max(maxsq,dp[i+1][j+1])
        
        return maxsq * maxsq
                    
        