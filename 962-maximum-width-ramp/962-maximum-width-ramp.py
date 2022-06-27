class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        
        def binary_search(stack,target):
            ans = -1
            l,r = 0,len(stack)-1
            while l <= r:
                mid = (l+r)//2
                if nums[stack[mid]] <= target:
                    ans = stack[mid]
                    r = mid-1
                else:
                    l = mid+1
            return ans
        
        for r in range(len(nums)):
            if stack and nums[r] >= nums[stack[-1]]:
                ans = max(ans,r-binary_search(stack,nums[r]))
            else:
                stack.append(r)
                
        return ans
        