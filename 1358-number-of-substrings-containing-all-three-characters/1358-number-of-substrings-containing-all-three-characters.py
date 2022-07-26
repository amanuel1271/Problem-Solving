class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq_cnt = defaultdict(int)
        l,cnt = 0,0
        
        for r in range(len(s)):
            freq_cnt[s[r]] += 1
            while l <= r and freq_cnt['a'] > 0 and freq_cnt['b'] > 0 and freq_cnt['c'] > 0:
                cnt += len(s)-r
                freq_cnt[s[l]] -= 1
                l += 1
        
        return cnt
                
            
        