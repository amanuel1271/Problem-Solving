class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        neg = [0 for _ in range(n)]
        pos = [0 for _ in range(n)]
        
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        
        ans = pos[0]
        
        for i in range(1,n):
            if nums[i] > 0:
                pos[i] = pos[i-1] + 1
                
                if neg[i-1] > 0:
                    neg[i] = neg[i-1] + 1
                    
            elif nums[i] < 0:
                neg[i] = pos[i-1] + 1
                
                if neg[i-1] > 0:
                    pos[i] = neg[i-1] + 1
                
            ans = max(ans,pos[i])
            
        return ans
            
            
        