class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_table = Counter(arr)
        delete_cnt,cnt = 0,0
        heap = []
        for num in freq_table:
            heapq.heappush(heap,-freq_table[num])
            
        while delete_cnt < len(arr)//2:
            delete_cnt +=  -heapq.heappop(heap)
            cnt += 1
            
        return cnt
            
            
            
        
            
        