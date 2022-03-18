class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minheap = []
        
        for stick in sticks:
            minheap.append(stick)
        
        heapify(minheap)
        
        cost  = 0
        
        while len(minheap) > 1:
            lowest  = heapq.heappop(minheap)
            second_lowest = heapq.heappop(minheap)
            
            cost += lowest + second_lowest
            heapq.heappush(minheap,lowest + second_lowest)
        
        return cost
            
            
            
        