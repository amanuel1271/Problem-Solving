class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        dp = [[0]*(i + 1) for i in range(height)]
        
        dp[-1] = triangle[-1]
        
        for i in range(height - 1):
            for j in range(len(triangle[-2-i])):
                dp[-2-i][j] = min(triangle[-2-i][j] + dp[-1-i][j],triangle[-2-i][j] + dp[-1-i][j+1])
                
        return min(dp[0])
