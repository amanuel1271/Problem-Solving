class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minn = 0

        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
                minn = mid if nums[mid] < nums[minn] else minn
                
        return nums[minn]