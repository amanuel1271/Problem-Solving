class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        size = len(changed)
        minheap = changed[:]
        heapify(minheap)
        
        original,seen = [],dict()
        
        while minheap:
            number = heappop(minheap)
            
            if number not in seen:
                seen[number] = 0
  
            if not (number % 2 == 0 and number//2 in seen and seen[number//2] > 0):            
                original.append(number)
                seen[number] += 1
            elif number % 2 == 0 and (number//2 in seen) and  seen[number//2] > 0:
                seen[number//2] -= 1

        print(original)    
        return original if size % 2 == 0 and len(original) * 2 == size else []
        
            
        
        
        