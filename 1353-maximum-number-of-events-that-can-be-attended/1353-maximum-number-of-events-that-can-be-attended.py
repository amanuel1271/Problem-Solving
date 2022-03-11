class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        n = max(events, key=lambda x: x[1])[1]
        
        cnt = 0
        i = 0
        for day in range(1, n+1):
            while i < len(events) and events[i][0] == day:
                heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heappop(heap)

            if heap:
                curr = heappop(heap)
                cnt += 1

        return cnt
            
            
                    
            
            