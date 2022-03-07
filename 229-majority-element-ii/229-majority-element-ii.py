class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = set()
        
        storecount = dict()
        
        for num in nums:
            if num in storecount:
                storecount[num] += 1
            else:
                storecount[num] = 1
            
            if storecount[num] > n//3 and num not in res:
                res.add(num)
        
        return list(res)
                
        