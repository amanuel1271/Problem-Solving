class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = math.inf
        second_num = math.inf
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False
        
        
       
        