class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch_freq,cnt,is_there_odd  = Counter(s),0,0
        for ch in ch_freq:
            if ch_freq[ch] % 2 == 0:
                cnt += ch_freq[ch]
            else:
                is_there_odd = 1
                cnt += ch_freq[ch] - 1
                
        return cnt + is_there_odd
        