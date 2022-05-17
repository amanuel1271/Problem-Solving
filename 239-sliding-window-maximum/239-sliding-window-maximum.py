class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,0
        output = []
        Q = deque()
        
        while r < len(nums):
            
            while Q and nums[Q[-1]] < nums[r]:
                Q.pop()
        
            Q.append(r)
            if l > Q[0]:
                Q.popleft()
                
            if r-l+1 == k:
                output.append(nums[Q[0]])
                l += 1  
                
            r += 1
            
        return output
                
            
        