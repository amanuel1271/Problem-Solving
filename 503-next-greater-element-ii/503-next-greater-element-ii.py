class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        indice_to_next = {}
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                indice_to_next[stack.pop()] = nums[i]
            stack.append(i)
            
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                indice_to_next[stack.pop()] = nums[i]
            
        return [indice_to_next.get(i,-1) for i in range(len(nums))]
        