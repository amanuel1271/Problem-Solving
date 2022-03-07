class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1 and (i,j) != (0,0):
                    obstacleGrid[i][j] = math.inf
                    continue
                if i > 0 and obstacleGrid[i-1][j] != math.inf:
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                if j > 0 and obstacleGrid[i][j-1] != math.inf:
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1]
                    
        return obstacleGrid[m-1][n-1]
                
                