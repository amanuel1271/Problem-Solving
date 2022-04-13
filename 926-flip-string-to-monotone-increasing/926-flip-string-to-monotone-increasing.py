class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = s.count('1')
        zeroes = len(s) - ones
        ones_so_far,store_zeroes_right = 0, [0 for _ in range(len(s))]
        ans = min(ones,zeroes)
        
        z = 0
        for i in range(len(s)-1,-1,-1):
            store_zeroes_right[i] = z
            z += (int(s[i]) + 1) % 2
            
        for j in range(len(s)):
            ones_so_far += int(s[j])
            ans = min(ans,ones_so_far + store_zeroes_right[j])
    
        return ans
                
            
        