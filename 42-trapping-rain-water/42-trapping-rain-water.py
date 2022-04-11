class Solution:
    def trap(self, height: List[int]) -> int:

        size = len(height)
        left_end,right_end = [0 for _ in range(size)],[0 for _ in range(size)]

        
        cur_max_left,cur_max_right = 0,0
        
        for i in range(size):
            cur_max_left = max(cur_max_left,height[i])
            left_end[i] = cur_max_left
            
        for j in range(size-1,-1,-1):
            cur_max_right = max(cur_max_right,height[j])
            right_end[j] = cur_max_right
            
        count = 0
        
        for i in range(size):
            minn = min(left_end[i],right_end[i])
            if minn > height[i]:
                count += minn - height[i]
                

        return count
        