class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows,columns = len(matrix),len(matrix[0])
        dp = [[0]*(columns+1) for _ in range(rows+1)]
        count = 0

        for i in range(1,rows+1):
            for j in range(1,columns+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                    count += dp[i][j]

        return count
                    
        

        