class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(k,vowels):
            if k == 1:
                return vowels
            if vowels == 1:
                return 1
            
            return helper(k-1,vowels) + helper(k,vowels-1)
        
        return helper(n,5)
        