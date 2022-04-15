class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for j in range(n+1):
            dp[m][j] = n-j
        for i in range(m+1):
            dp[i][n] = m-i
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(1 + dp[i][j+1],1 + dp[i+1][j],1 + dp[i+1][j+1])
        
        return dp[0][0]
        
#         @lru_cache(None)
#         def helper(i,j):
#             if i == len(word1) and j == len(word2):
#                 return 0
#             if i == len(word1):
#                 return len(word2) - j
#             if j == len(word2):
#                 return len(word1) - i


#             if word1[i] == word2[j]:
#                 ans = helper(i + 1, j + 1)
#             else: 
#                 insert = 1 + helper(i, j + 1)
#                 delete = 1 + helper( i + 1, j)
#                 replace = 1 + helper(i + 1, j + 1)
#                 ans = min(insert, delete, replace)
                
#             return ans
        
#         return helper(0,0)
        