class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        size = len(s)
        if size < k:
            return False
        
        count = Counter(s)
        odd_count = 0
        
        for ch,cnt in count.items():
            if cnt % 2 == 1:
                odd_count += 1
                
        if odd_count > k:
            return False
        
        return True
        