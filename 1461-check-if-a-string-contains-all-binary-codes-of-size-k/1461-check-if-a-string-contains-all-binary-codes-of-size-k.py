class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_set = set()
        
        for i in range(len(s)-k + 1):
            binary_set.add(s[i:i+k])
            if len(binary_set) == 2**k:
                return True
            
        return False
        