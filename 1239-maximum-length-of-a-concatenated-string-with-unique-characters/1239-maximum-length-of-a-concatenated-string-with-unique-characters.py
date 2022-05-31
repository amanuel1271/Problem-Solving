class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        unique = ['']
        

        for word in arr:
            for j in unique:
                tmp = word + j
                if len(tmp) == len(set(tmp)): # no overlapping chars
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))
                    
        return maxlen