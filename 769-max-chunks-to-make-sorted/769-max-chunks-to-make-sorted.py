class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        
        for num in arr:
            largest = num
            while stack and num < stack[-1]:
                largest = max(largest,stack.pop())
        
            stack.append(largest)
            
        return len(stack)