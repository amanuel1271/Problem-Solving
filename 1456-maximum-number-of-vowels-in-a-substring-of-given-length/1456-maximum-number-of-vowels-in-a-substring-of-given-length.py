class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        l,cnt = 0,sum(1 for ch in s[:k] if ch in vowels)
        max_cnt = cnt
        
        for r in range(k,len(s)):
            cnt = cnt + 1 if s[r] in vowels else cnt
            cnt = cnt - 1 if s[l] in vowels else cnt
            l += 1
            max_cnt = max(max_cnt,cnt)
        return max_cnt
            
        
        
        