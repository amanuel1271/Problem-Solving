class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        
        
        for k in range(len(nums)):
            if stack and nums[k] >= nums[stack[-1]]:
                for i in range(len(stack)-1,-1,-1):
                    if nums[k] >= nums[stack[i]]:
                        ans = max(ans,k-stack[i])
                    else:
                        break
            else:
                stack.append(k)
                
        return ans
        