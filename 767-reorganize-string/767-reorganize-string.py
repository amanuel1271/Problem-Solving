class Solution:
    def reorganizeString(self, s: str) -> str:
        prev = None
        maxheap = []
        count = Counter(s)
        size = len(s)
        
        for key in count:
            maxheap.append((-count[key],key))
            
        heapify(maxheap)
        ans = ''
        ansSize = 0
        
        while True:
            if ansSize == size:
                break
            
            if maxheap:
                revCount,ch  = heappop(maxheap)
            
            if prev == None:
                ans += ch
                ansSize += 1
                prev = (revCount + 1,ch)
            elif revCount <= -1 and ch != prev[1]:
                ans += ch
                ansSize += 1
                
                heappush(maxheap,prev)
                prev = (revCount + 1,ch)
            else:
                return ''
        
            
        return ans
            
        
            
        
        
        
        
                    
            
                
        