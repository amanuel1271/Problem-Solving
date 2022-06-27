class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        
        
        for j in range(len(nums)):
            if stack and nums[j] >= nums[stack[-1]]:
                for i in range(len(stack)-1,-1,-1):
                    if nums[j] >= nums[stack[i]]:
                        ans = max(ans,j-stack[i])
                    else:
                        break
            else:
                stack.append(j)
                
        return ans
        