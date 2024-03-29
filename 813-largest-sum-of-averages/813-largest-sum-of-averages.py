class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        @lru_cache(None)
        def search(n, k):
            if n < k: return 0
            elif n == k:
                return sum(nums[:n])
            elif k == 1:
                return  float(sum(nums[:n]) / n)
            
            cur,res = 0,0
            for i in range(n - 1, -1, -1):
                cur += nums[i]
                res = max(res, search(i, k - 1) + float(cur /(n - i)) )
            return res
        
        return search(len(nums), k)