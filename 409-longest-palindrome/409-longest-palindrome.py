class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch_freq  = Counter(s)
        cnt_to_char = [ch_freq[ch] for ch in ch_freq]
        
        def max_odd():
            odd_list = list(filter(lambda x: (x%2 == 1),cnt_to_char))
            if len(odd_list) == 0:
                return 0,0
            
            maxx = max(odd_list)
            rest_sum = sum(odd_list) - maxx - len(odd_list) + 1
            return maxx,rest_sum
            
        even_list = list(filter(lambda x: (x%2 == 0),cnt_to_char))
        return sum(max_odd()) + sum(even_list)
        