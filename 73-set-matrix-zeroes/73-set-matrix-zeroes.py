class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m,n = len(matrix),len(matrix[0])
        visit,row_seen,col_seen = set(),set(),set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visit.add((i,j))
                    
        while visit:
            row,col = visit.pop()
            if row not in row_seen:
                for c in range(n):
                    matrix[row][c] = 0
                row_seen.add(row)  
            if col not in col_seen:
                for r in range(m):
                    matrix[r][col] = 0
                col_seen.add(col)
                
                    
                    