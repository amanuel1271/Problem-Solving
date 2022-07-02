class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:\
        
        def second_arr(arr):
            l,r = 0,secondLen-1
            window_sum = sum(arr[l:r+1])
            maxx = window_sum
            r += 1
            
            while r < len(arr):
                window_sum += arr[r]
                window_sum -= arr[l]
                l += 1
                maxx = max(maxx,window_sum)
                r += 1
            return maxx
        
        def firstarr():
            l,r = 0,firstLen-1
            window_sum = sum(nums[l:r+1])
            maxx = window_sum + second_arr(nums[:l] + nums[r+1:])
            r += 1
            
            while r < len(nums):
                window_sum += nums[r]
                window_sum -= nums[l]
                l += 1
                
                cand = window_sum + second_arr(nums[:l] + nums[r+1:])
                maxx = max(maxx,cand)
                r += 1
                
            return maxx
        
        return firstarr()
                
            
            
        