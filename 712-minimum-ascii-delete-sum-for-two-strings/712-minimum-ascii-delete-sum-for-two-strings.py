class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        row,col = len(s1),len(s2)
        dp = [[0]*(col+1) for _ in range(row+1)]
        
        for i in range(row):
            dp[i][col] = sum([ord(ch) for ch in s1[i:]])
        for j in range(col):
            dp[row][j] = sum([ord(ch) for ch in s2[j:]])
            
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),dp[i][j+1] + ord(s2[j]))
            
        return dp[0][0]
        