class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
            
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = i
            
                
        for op in range(len(operations)):
                i = index[operations[op][0]]
                del index[nums[i]]
                nums[i] = operations[op][1]
                index[nums[i]] = i
            
            
            
        return nums
        