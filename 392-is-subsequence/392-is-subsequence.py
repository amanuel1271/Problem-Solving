class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r = 0,0
        bound_1,bound_2 = len(s),len(t)
        
        
        while l < bound_1 and r < bound_2:
            if s[l] == t[r]:
                l += 1
            r += 1
            
        return l == bound_1
        