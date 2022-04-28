class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        count = [0]*(target + 1)
        count[0] = 1
        
        for trg in range(1,target+1):
            for num in nums:
                if trg-num >= 0:
                    count[trg] += count[trg-num]
                    
        return count[-1]
            
    
                    
        
            
            
            
            
            
        
            
        