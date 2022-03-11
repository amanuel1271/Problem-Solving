class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        size = len(events)
        heap = []
        n = max(events, key=lambda x: x[1])[1]
        
        cnt = 0
        i = 0
        for day in range(1, n+1):
            while i < size and events[i][0] <= day <= events[i][1]:
                heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heappop(heap)

            if heap:
                curr = heappop(heap)
                cnt += 1

        return cnt
    
            
            
                    
            
            