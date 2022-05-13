class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        
        for num in arr:
            largest = num
            while stack and stack[-1] > num:
                largest = max(largest,stack.pop())
        
            stack.append(largest)
            
        return len(stack)