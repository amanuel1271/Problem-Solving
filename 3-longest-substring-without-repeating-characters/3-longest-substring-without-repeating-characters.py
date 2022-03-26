class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count,max_count = 0,-math.inf
        
        for i,ch in enumerate(s):
            visited = {ch}
            count = 1
            for j in range(i+1,len(s)):
                if s[j] in visited:
                    break
                count += 1
                visited.add(s[j])
                
            max_count = max(count,max_count)
            
        max_count = max(count,max_count)
        return max_count
                
            
        