class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = [] 
        num_of_buildings = len(heights)
        
        for i in range(num_of_buildings-1):
            climb = heights[i + 1] - heights[i]
            if climb > 0:
                heapq.heappush(ladder_allocations, climb)
                if len(ladder_allocations) > ladders:
                    bricks -= heapq.heappop(ladder_allocations)
                    if bricks < 0:
                        return i

        return num_of_buildings-1
        