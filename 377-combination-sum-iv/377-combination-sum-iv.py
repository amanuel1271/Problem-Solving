class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        count = [0]*(target + 1)
        count[0] = 1
        
        for trg in range(1,target+1):
            for num in nums:
                if trg-num >= 0:
                    count[trg] += count[trg-num]
                    
        return count[-1]
            
        
#         @lru_cache(None)
#         def add_up(trg):
#             if trg == 0:
#                 return 1
            
            
#             count = 0
            
#             for num in nums:
#                 if trg-num >= 0:
#                     count += add_up(trg-num)
                    
#             return count
        
#         return add_up(target)
                    
        
            
            
            
            
            
        
            
        