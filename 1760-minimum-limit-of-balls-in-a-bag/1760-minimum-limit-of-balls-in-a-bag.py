class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def isPossible(penalty):
            count = 0
            for num in nums:
                operations = num // penalty
                if num % penalty  == 0:
                    operations -= 1
                count += operations 
            return count <= maxOperations
        
        minn,left,right = 0,1,max(nums)
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                minn = mid
                right = mid-1
            else:
                left  = mid + 1
                
        return minn
                
        
        
        