class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        @lru_cache(None)
        def search(n, k):
            if n < k: return 0
            if k == 1:
                return  sum(nums[:n]) / float(n)
            
            cur,res = 0,0
            for i in range(n - 1, -1, -1):
                cur += nums[i]
                res = max(res, search(i, k - 1) + (cur / float(n - i)))
            return res
        
        return search(len(nums), k)