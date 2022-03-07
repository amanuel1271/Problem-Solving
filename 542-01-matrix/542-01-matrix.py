class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        
        cells = deque()
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    cells.append((i, j - 1, 1))
                    cells.append((i, j + 1, 1))
                    cells.append((i - 1, j, 1))
                    cells.append((i + 1, j, 1))
        
        while cells:
            row, col, distance = cells.popleft()
            
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                mat[row][col] = distance
                visited.add((row, col))
                cells.append((row, col - 1, distance + 1))
                cells.append((row, col + 1, distance + 1))
                cells.append((row - 1, col, distance + 1))
                cells.append((row + 1, col, distance + 1))
                
        return mat
                        
                    
            
                    