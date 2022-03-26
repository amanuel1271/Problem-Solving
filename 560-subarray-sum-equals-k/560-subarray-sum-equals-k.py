class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count,cum_sum = 0,0
        hashmap = dict()
        hashmap[0] = 1
        
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in hashmap:
                count += hashmap[cum_sum-k]
                
            hashmap[cum_sum] = hashmap.get(cum_sum,0) + 1
        
        return count
        
        
            
        