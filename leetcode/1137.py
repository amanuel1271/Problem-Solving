class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
            
        dp = [0] * (n + 1)
        
        dp[0],dp[1],dp[2] = 0,1,1
        
        for j in range(3,n + 1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        
        return dp[n]
