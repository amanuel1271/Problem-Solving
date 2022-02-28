class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        
        minHeap = []
        for r in range(N):
            minHeap.append((matrix[r][0], r, 0))
        
        heapify(minHeap)    
        

        while k > 0:
            element, r, c = heappop(minHeap)
            if c < N - 1:
                heappush(minHeap, (matrix[r][c+1], r, c+1))
            k -= 1
        
        return element
