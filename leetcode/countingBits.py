class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] *(n+1)
        if n == 0:
            return dp
        dp[1] = 1
        if n == 1:
            return dp
        
        dp[2] = 1
        save = 2
        
        for j in range(2,n+1):
            if j == save:
                dp[j] = 1
                save *= 2
                continue
            dp[j] = 1 + dp[j - save//2]
        return dp
