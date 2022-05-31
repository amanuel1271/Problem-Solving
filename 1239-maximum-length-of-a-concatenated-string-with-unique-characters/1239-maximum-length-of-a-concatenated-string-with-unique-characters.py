class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        unique = ['']
        
        def isvalid(s):
            return len(s) == len(set(s))
        
        for word in arr:
            for j in unique:
                tmp = word + j
                if isvalid(tmp):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))
                    
        return maxlen