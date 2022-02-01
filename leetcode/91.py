class Solution:
    def numDecodings(self, s: str) -> int:
        strnum_to_alpha = dict()
        for num in range(1,27):
            strnum_to_alpha[str(num)] =  chr(ord('A') + (num-1))
        
        @lru_cache(None)
        def dp(word):
            lenn = len(word)
            
            if lenn == 1:
                if word == '0':
                    return 0
                return 1
            elif lenn == 2:
                if word in strnum_to_alpha:
                    if word[0] in strnum_to_alpha and word[1] in strnum_to_alpha:
                        return 2
                    else:
                        return 1
                else:
                    if word[0] in strnum_to_alpha and word[1] in strnum_to_alpha:
                        return 1
                    else:
                        return 0
            
            first,second = dp(word[0]),0 
            if (word[0:2] in strnum_to_alpha):
                second = dp(word[2:])
                
            if first == 0:
                return second
                
            
            return dp(word[1:]) + second
        
        return dp(s)
