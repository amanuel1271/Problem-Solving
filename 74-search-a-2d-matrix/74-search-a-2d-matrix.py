class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        
        def low_binary_search():
            left,right = 0,r-1
            ans = -1
            while left <= right:
                mid = (left+right)//2
                if matrix[mid][0] == target:
                    return mid
                elif matrix[mid][0] > target:
                    right = mid-1
                else:
                    ans = mid
                    left = mid+1
            return ans
                    
        search_row = low_binary_search()
        if matrix[search_row][0] == target:
            return True
        
        def vanilla_bs():
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
        return vanilla_bs()
            
                    
        