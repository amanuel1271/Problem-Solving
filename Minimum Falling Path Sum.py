class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for row in range(1,n):
            for col in range(n):
                above = matrix[row-1][col]
                
                if 0 <= col-1 < n:
                    left_dg = matrix[row-1][col-1]
                else:
                    left_dg = math.inf
                if 0 <= col+1 < n:
                    right_dg = matrix[row-1][col+1]
                else:
                    right_dg = math.inf
                    
                matrix[row][col] += min(above,left_dg,right_dg)
                
        return min(matrix[n-1])
