class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count,s_count = Counter(p),{}
        size_s,size_p = len(s) + 1,len(p)
        
        l,r,res = 0,size_p-1,[]
        s = ' ' + s
        if size_s < size_p:
            return []
        
        
        
        for i in range(r+1):
            s_count[s[i]] = s_count.get(s[i],0) + 1
        
        while r < size_s - 1:
            r += 1
            s_count[s[r]] = s_count.get(s[r],0) + 1
            s_count[s[l]] = s_count.get(s[l],0) - 1
            equal = True
            
            for ch,cnt in p_count.items():
                if s_count.get(ch,0) != cnt:
                    equal = False
                    break
                    
            if equal:
                res.append(l)
            l += 1
            
        return res
            
            
            
            
        