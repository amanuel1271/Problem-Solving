class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for row in range(1,n):
            for col in range(n):
                above = matrix[row-1][col]
                left_dg = matrix[row-1][col-1] if 0 <= col-1 < n else math.inf
                right_dg = matrix[row-1][col+1] if 0 <= col+1 < n else math.inf   
                matrix[row][col] += min(above,left_dg,right_dg)
                
        return min(matrix[n-1])
