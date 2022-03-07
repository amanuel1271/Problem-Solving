class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_val(x):
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 1 + 3 * x
                count += 1
                
            return count
                
        return sorted([num for num in range(lo,hi+1)],key = lambda x: power_val(x))[k-1]
                    
        