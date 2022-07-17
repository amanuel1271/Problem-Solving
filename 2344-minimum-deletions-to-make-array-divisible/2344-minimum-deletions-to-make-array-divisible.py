class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            
            return gcd(b,a%b)
        
        # find gcd
        gcd_res = numsDivide[0]
        for num in numsDivide[1:]:
            gcd_res = gcd(gcd_res,num)
            
        nums.sort()
        for i in range(len(nums)):
            if gcd_res % nums[i] == 0:
                return i
            
        return -1
            
        
            
        
            