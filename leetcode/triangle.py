class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 1):
            for j in range(len(triangle[-2-i])):
                triangle[-2-i][j] = min(triangle[-2-i][j] + triangle[-1-i][j],triangle[-2-i][j] + triangle[-1-i][j+1]) 
                
        return min(triangle[0])
