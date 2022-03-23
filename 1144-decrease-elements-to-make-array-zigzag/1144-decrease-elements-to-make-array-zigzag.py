class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        copy,size = nums[:],len(nums)
        move_1,move_2 = 0,0
        
        def find_valley(i,arr):
            left,right = math.inf,math.inf
            if i-1 >= 0:
                left = arr[i-1]
            if i+1 <= size - 1:
                right = arr[i+1]
                
            return min(left,right) - 1
        
        
        for i in range(1,size):
            if i % 2:
                minn = find_valley(i,copy)
                if copy[i] <= minn:
                    continue
                move_1 += copy[i] - minn
                copy[i] = minn
        for i in range(size):
            if i % 2 == 0:
                minn = find_valley(i,nums)
                if nums[i] <= minn:
                    continue
                move_2 += nums[i] - minn
                nums[i] = minn
                
                
        return min(move_1,move_2)
