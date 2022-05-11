class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextgreater = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                nextgreater[stack.pop()] = num
            stack.append(num)
            
        return map(lambda num: nextgreater.get(num,-1),nums1)
        