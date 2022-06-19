class Solution:
    def greatestLetter(self, s: str) -> str:
        maxx = 0
        ch_map = dict()
        
        
        for ch in s:
            if ch not in ch_map:
                ch_map[ch] = True
            
            if ch.lower() in ch_map and ch.upper() in ch_map:
                maxx = max(maxx,ord(ch.upper()))
                
                
        return '' if maxx == 0 else chr(maxx)