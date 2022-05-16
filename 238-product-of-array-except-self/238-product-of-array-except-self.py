class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right,left = [],[]
        size = len(nums)
        
        cur = 1
        for num in nums:
            cur *= num
            right.append(cur)
            
        cur = 1
        for i in range(size-1,-1,-1):
            cur *= nums[i]
            left.append(cur)
        left.reverse()
        
        ans = [0]*size
        for i in range(size):
            if i == 0:
                ans[i] = left[i+1]
                continue
            elif i == size - 1:
                ans[i] = right[i-1]
                continue
            
            ans[i] = right[i-1]*left[i+1]
            
        return ans