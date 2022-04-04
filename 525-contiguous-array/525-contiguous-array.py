class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_to_indices = defaultdict(list)
        count = 0
        res = 0
        count_to_indices[0].append(-1)
        
        for i in range(len(nums)):
            count = count + 1 if nums[i] == 1 else count - 1
            count_to_indices[count].append(i)
            
            
        for cnt in count_to_indices:
            res = max(res,count_to_indices[cnt][-1] - count_to_indices[cnt][0])
            
        return res
            
        