class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search():
            l,r = 0,len(nums)-1
            while l < r:
                mid = (l+r)//2
                if nums[mid] == target:
                    r = mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1       
            return l if nums[l] == target else -1
        
        if not nums:
            return [-1,-1]
        
        l = binary_search()
        return [l,bisect.bisect_left(nums, target + 1)-1] if l != -1 else [-1,-1]
        
        