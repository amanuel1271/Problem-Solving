class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_chars = {}
        mapped_set = set()
        
        for i in range(len(s)):
            if s[i] in map_chars and t[i] != map_chars[s[i]]:
                return False
            elif t[i] in mapped_set and s[i] not in map_chars:
                return False
            elif s[i] not in map_chars:
                map_chars[s[i]] = t[i]
                mapped_set.add(t[i])
                
        return True
            
        