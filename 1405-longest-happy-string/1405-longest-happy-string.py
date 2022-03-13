class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''
        prev = None
        maxheap = []
                    
        for ch in ['a','b','c']:
            if ch == 'a' and a > 0:
                maxheap.append((-a,'a'))
            elif ch == 'b' and b > 0:
                maxheap.append((-b,'b'))
            elif ch == 'c' and c > 0:
                maxheap.append((-c,'c'))
                
        heapify(maxheap)

        while True:
            if not maxheap:
                break
                
            rcount, ch = heappop(maxheap)
            if (not prev and rcount <= -2) or (rcount <= -2 and rcount < prev[0]):
                ans += ch * 2
                rcount += 2
            else:
                ans += ch 
                rcount += 1
                
            if prev != None:
                if prev[0] < 0:
                    heappush(maxheap,prev)
            
            prev = (rcount,ch)
        
        return ans
            
            
                
                
            
        