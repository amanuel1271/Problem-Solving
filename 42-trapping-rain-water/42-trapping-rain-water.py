class Solution:
    def trap(self, height: List[int]) -> int:

        size = len(height)
        count = 0
        l,r = 0,size-1
        cur_max_left,cur_max_right = 0,0
        
        while l < r:
            if height[l] < height[r]:
                cur_max_left = max(cur_max_left,height[l])
                count += cur_max_left - height[l]
                l += 1
            else:
                cur_max_right = max(cur_max_right,height[r])
                count += cur_max_right - height[r]
                r -= 1
                

        return count
        