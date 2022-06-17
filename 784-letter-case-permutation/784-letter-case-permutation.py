class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        size = len(s)
        
        def construct(i,constructed_string):
            if i == size:
                res.append(constructed_string)
                return
            
            ch = s[i]
            if ch.isalpha():
                construct(i+1,constructed_string + ch.lower())
                construct(i+1,constructed_string + ch.upper())
            else:
                construct(i+1,constructed_string + ch)
                
        
        construct(0,'')
        return res
            
        