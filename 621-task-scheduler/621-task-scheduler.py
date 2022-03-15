class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapify(maxheap)
        
        time = 0
        Q = deque()
        
        while maxheap or Q:
            time += 1
            
            if maxheap:
                cnt = 1 + heappop(maxheap)
                
                if cnt:
                    Q.append([cnt,time + n])
            
            if Q and Q[0][1] == time:
                heappush(maxheap,Q.popleft()[0])
        
        return time
                    
                
                
        