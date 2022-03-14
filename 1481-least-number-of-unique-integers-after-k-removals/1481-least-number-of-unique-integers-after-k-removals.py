class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        minheap = []
        num_to_count = Counter(arr)
        for num,count in num_to_count.items():
            minheap.append((count,num))
        heapify(minheap)
        
        for _ in range(k):
            cnt,number = heappop(minheap)
            if cnt > 1:
                heappush(minheap,(cnt-1,number))
        
        
        return len(minheap)
            