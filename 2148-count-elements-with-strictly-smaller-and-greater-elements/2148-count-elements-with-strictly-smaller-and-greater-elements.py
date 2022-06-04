class Solution:
    def countElements(self, nums: List[int]) -> int:
        minn,maxx = min(nums),max(nums)
        return sum([1 for num in nums if minn < num < maxx])
        
        