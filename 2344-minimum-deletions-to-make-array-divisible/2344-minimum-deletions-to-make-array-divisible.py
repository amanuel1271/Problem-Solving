class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a
        
        # find gcd
        gcd_res = numsDivide[0]
        for num in numsDivide[1:]:
            gcd_res = gcd(gcd_res,num)
            
        nums.sort()
        for i in range(len(nums)):
            if gcd_res % nums[i] == 0:
                return i
            
        return -1
            
        
            
        
            