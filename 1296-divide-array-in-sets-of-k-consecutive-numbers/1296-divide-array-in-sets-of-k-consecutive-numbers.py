class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:       
        if len(nums) % k != 0:
            return False
        
        count = collections.Counter(nums)
        for n in sorted(count):
            if count[n] > 0:
                need = count[n]
                for i in range(n,n+k):
                    if count[i] < need:
                        return False
                    count[i] -= need
        return True
        
        

        