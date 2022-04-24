class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r,c = len(s),len(t)
        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        
        for row in range(r-1,-1,-1):
            for col in range(c-1,-1,-1):
                if s[row] == t[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col],dp[row][col + 1])
                    
        return dp[0][0] == r
        