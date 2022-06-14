class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n  = len(grid),len(grid[0])
        maxArea = 0
        visited = set()
        
        
        def islandArea(row,col):
            count = 1
            
            for next_row,next_col in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                if 0 <= next_row < m and 0 <= next_col < n and (next_row,next_col) not in visited:
                    if grid[next_row][next_col] == 1:
                        visited.add((next_row,next_col))
                        count += islandArea(next_row,next_col)
        
            return count
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row,col) not in visited:
                    visited.add((row,col))
                    maxArea = max(maxArea,islandArea(row,col))
                    
        
        return maxArea