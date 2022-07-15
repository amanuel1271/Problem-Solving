class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total,cur_window_total,cur_window_cnt = 0,0,0
        l = 0
        
        for r in range(len(nums)):
            cur_window_cnt += (nums[r] % 2)
            
            if cur_window_cnt < k:
                continue 
            elif cur_window_cnt == k:
                cur_window_total += 1
                if r < len(nums)-1 and nums[r+1]%2 == 0:
                    continue
              
            l0 = l
            while (nums[l] % 2) == 0 and l <= r:
                l += 1
                
            total += (l-l0+1)* cur_window_total
            cur_window_total,cur_window_cnt = 0,cur_window_cnt-1
            l += 1
            
        return total
            
        
            
                