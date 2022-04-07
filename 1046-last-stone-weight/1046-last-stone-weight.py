class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_size = len(stones)
        for i in range(stones_size):
            stones[i] *= -1
        heapify(stones)
        
        while stones_size > 1:
            y = -1 * heappop(stones)
            x = -1 * heappop(stones)
            stones_size -= 2
            
            if x != y:
                heappush(stones,x-y)
                stones_size += 1
                
        return 0 if stones_size == 0 else -1 * stones[0]
            
            