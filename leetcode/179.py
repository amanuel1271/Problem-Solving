class Solution(object):
    def largestNumber(self, nums):
        def compare(str1,str2):
            if str1+str2 > str2+str1:
                return True
            return False
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if compare(str(nums[j]),str(nums[j+1])):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    
        res = ''
        
        for j in range(len(nums)-1,-1,-1):
            res += str(nums[j])
        
        return '0' if int(res) == 0 else res
