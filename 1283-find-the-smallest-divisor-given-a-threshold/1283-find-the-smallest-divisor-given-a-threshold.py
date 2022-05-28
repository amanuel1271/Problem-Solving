class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def divide_array(divisor):
            return sum([math.ceil(num/divisor) for num in nums])
        
        left,right = 1,max(nums)
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if divide_array(mid) > threshold:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
                
        return ans
            
        
        