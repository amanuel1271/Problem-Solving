class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*(n) for _ in range(m)]
        maxsq = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                    maxsq = max(maxsq,dp[i][j])
        
        return maxsq * maxsq
                    
        