class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @lru_cache(None)
        def delete(i,j):
            if i == len(s1):
                return sum([ord(ch) for ch in s2[j:]])
            elif j == len(s2):
                return sum([ord(ch) for ch in s1[i:]])
            
            if s1[i] == s2[j]:
                return delete(i+1,j+1)
            
            return min(delete(i+1,j) + ord(s1[i]),delete(i,j+1) + ord(s2[j]))
            
        return delete(0,0)
        