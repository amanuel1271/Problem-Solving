class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        
        
        def vanilla_bs(search_row):
            left,right = 0,c-1
            while left <= right:
                mid = (left+right)//2
                if matrix[search_row][mid] == target:
                    return True
                elif matrix[search_row][mid] > target:
                    right = mid-1
                else:
                    left = mid+1   
            return False
        
        
        for i in range(r):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                return False
            
            if vanilla_bs(i):
                return True
            
        return False
        