class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        size = len(changed)
        minheap = changed[:]
        heapify(minheap)
        seen = defaultdict(int)
        
            
        
        original = []
        
        while minheap:
            number = heappop(minheap)
            if not (number % 2 == 0 and seen[number//2] > 0):            
                original.append(number)
                seen[number] += 1
            elif number % 2 == 0 and  seen[number//2] > 0:
                seen[number//2] -= 1
 
        return original if size % 2 == 0 and len(original) * 2 == size else []
        
            
        
        
        