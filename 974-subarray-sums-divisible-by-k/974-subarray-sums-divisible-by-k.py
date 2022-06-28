class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modulo_dict = defaultdict(int)
        modulo_dict[0],count,prefix_sum = 1,0,0
        
        for num in nums:
            prefix_sum += num
            count += modulo_dict[prefix_sum%k]
            modulo_dict[prefix_sum%k] += 1
            
        return count
            