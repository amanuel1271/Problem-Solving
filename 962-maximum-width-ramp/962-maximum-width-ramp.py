class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        
        
        for r in range(len(nums)):
            if stack and nums[r] >= nums[stack[-1]]:
                for i in range(len(stack)-1,-1,-1):
                    if nums[r] >= nums[stack[i]]:
                        ans = max(ans,r-stack[i])
                    else:
                        break
            else:
                stack.append(r)
                
        return ans
        