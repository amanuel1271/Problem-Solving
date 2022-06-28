class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [(x**2 + y**2,x,y) for x,y in points]
        heapq.heapify(minheap)
        ans = []
        
        
        for i in range(k):
            dist,x,y = heapq.heappop(minheap)
            ans.append([x,y])
            
        return ans
            