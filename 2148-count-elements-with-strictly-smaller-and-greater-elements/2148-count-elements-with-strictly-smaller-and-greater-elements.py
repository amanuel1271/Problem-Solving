class Solution:
    def countElements(self, nums: List[int]) -> int:
        minn,maxx = min(nums),max(nums)
        count = 0
        
        for num in nums:
            if minn < num < maxx:
                count += 1
        
        return count
        
        