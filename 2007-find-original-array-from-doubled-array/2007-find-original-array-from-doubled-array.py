class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        minheap,original = changed[:],[]
        heapify(minheap)
        seen,size = defaultdict(int),len(changed)
        
        while minheap:
            number = heappop(minheap)
            if number % 2 == 0 and seen[number//2] > 0:
                seen[number//2] -= 1
            else:
                original.append(number)
                seen[number] += 1
                
 
        return original if size % 2 == 0 and len(original) * 2 == size else []
        
            
        
        
        