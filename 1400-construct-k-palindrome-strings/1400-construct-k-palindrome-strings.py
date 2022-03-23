class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        odd_count = 0
        for ch,cnt in Counter(s).items():
            if cnt % 2 == 1:
                odd_count += 1
                
        if odd_count > k:
            return False
        
        return True
        