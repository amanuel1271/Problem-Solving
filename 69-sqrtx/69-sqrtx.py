class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 1,x
        ans = 0
        
        while left <= right:
            mid = (left + right)//2
            if mid**2  <= x:
                left = mid + 1
                ans = mid
            else:
                right = mid-1
                
        return ans
        