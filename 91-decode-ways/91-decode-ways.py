class Solution:
    def numDecodings(self, s: str) -> int:
        strnum_to_alpha = dict()
        for num in range(1,27):
            strnum_to_alpha[str(num)] =  chr(ord('A') + (num-1))
        
        @lru_cache(None)
        def dp(word):
            l = len(word)
            
            if l == 1:
                return 0 if word == '0' else 1
            elif l == 2:
                if word in strnum_to_alpha:
                    return 2 if word[0] in strnum_to_alpha and word[1] in strnum_to_alpha else 1       
                else:
                    return 1 if word[0] in strnum_to_alpha and word[1] in strnum_to_alpha else 0
            
            first,second = dp(word[0]),0 
            if (word[0:2] in strnum_to_alpha):
                second = dp(word[2:])  
            if first == 0:
                return second
            return dp(word[1:]) + second
        
        return dp(s)
                    
            
            
        