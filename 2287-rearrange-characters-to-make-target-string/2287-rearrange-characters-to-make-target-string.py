class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_,t,count = {},{},math.inf
        for ch in target:
            t[ch] = t.get(ch,0) + 1
            
        for ch in s:
            if ch in t:
                s_[ch] = s_.get(ch,0) + 1
        
        

        for ch in t:
            count = min(count,s_.get(ch,0)//t[ch])
                
        return count if count != math.inf else 0