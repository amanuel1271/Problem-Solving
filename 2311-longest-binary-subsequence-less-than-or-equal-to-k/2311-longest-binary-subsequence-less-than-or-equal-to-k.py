class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cnt,val = 0,0
        
        i = len(s)-1
        while i >= 0:
            val += (2 ** cnt) * (ord(s[i]) - ord('0'))
            if val > k:
                break
                
            cnt += 1
            i -= 1
            
        return s[:i+1].count('0') + cnt
        