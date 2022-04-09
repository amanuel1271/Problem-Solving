class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        
        for num in nums:
            num_set.add(num)
            
        longest_streak = 0
        
        for num in num_set:
            if num-1 not in num_set:
                cur = num
                streak = 1
                
                while cur+1 in num_set:
                    cur += 1
                    streak += 1
                    
                longest_streak = max(longest_streak,streak)
                
        return longest_streak
                
            
        
        
        