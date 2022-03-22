class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        copy,size = nums[:],len(nums)
        move_1,move_2 = 0,0
        
        for i in range(1,size):
            if i % 2:
                left,right = math.inf,math.inf
                if i-1 >= 0:
                    left = copy[i-1]
                if i+1 <= size - 1:
                    right = copy[i+1]
                    
                minn = min(left,right) - 1
                if copy[i] <= minn:
                    continue
                move_1 += copy[i] - minn
                copy[i] = minn
        
        for i in range(size):
            if i % 2 == 0:
                left,right = math.inf,math.inf
                if i-1 >= 0:
                    left = nums[i-1]
                if i+1 <= size - 1:
                    right = nums[i+1]
                    
                minn = min(left,right) -1
                if nums[i] <= minn:
                    continue
                    
                move_2 += copy[i] - minn
                copy[i] = minn
                
                
        return min(move_1,move_2)