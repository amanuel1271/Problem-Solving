class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = Counter(nums)
        minheap = []
        
        for num,cnt in count.items():
            minheap.append((-cnt,num))
            
            
        heapify(minheap)
        ans = []
        
        for _ in range(k):
            ans.append(heappop(minheap)[1])
        
        return ans
            
        