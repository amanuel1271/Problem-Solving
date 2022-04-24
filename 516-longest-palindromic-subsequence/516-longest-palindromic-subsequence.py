class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @lru_cache(None)
        def maxMatchCount(left, right):           
            if left > right:
                return 0
            
            if left == right:
                return 1            
            
            if s[left] == s[right]:
                return maxMatchCount(left+1, right-1) + 2
            else:
                return max(maxMatchCount(left+1, right), maxMatchCount(left, right-1))
        
        return maxMatchCount(0,len(s)-1)
        