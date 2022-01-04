class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [[0] * n for i in range(m)]
        dp[m-1][n-1] = 0
        
        for i in range(m - 1):
            dp[i][n-1] = 1
        for i in range(n - 1):
            dp[m-1][i] = 1
            
        for i in range(n - 1):
            for j in range(m - 1):
                dp[-2-j][-2-i] = dp[-2-j][-1-i] + dp[-1-j][-2-i]
                
        return dp[0][0]
