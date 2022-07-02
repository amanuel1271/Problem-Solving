class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:\
        
        def slide(r_len):
            l_len = firstLen + secondLen - r_len
            
            # boundary of the left window and right window
            r_l,r_r = len(nums)-r_len,len(nums)-1
            l_r = r_l-1
            l_l = l_r - (l_len - 1)
            
            left_window_sum,right_window_sum = sum(nums[l_l : l_r+1]),sum(nums[r_l:r_r+1])
            r_max = right_window_sum
            max_val = left_window_sum + r_max
            l_l -= 1
            r_l -= 1
            
            
            while l_l >= 0:
                left_window_sum += nums[l_l]
                left_window_sum -= nums[l_r]
                l_r -= 1
                right_window_sum += nums[r_l]
                right_window_sum -= nums[r_r]
                r_r -= 1
                
                r_max = max(r_max,right_window_sum)
                max_val = max(max_val, r_max + left_window_sum)
                l_l -= 1
                r_l -= 1
                
            return max_val
                
                
                

        return max(slide(firstLen),slide(secondLen))
                
            
            
        