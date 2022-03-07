class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums2),len(nums1)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        output = -math.inf
        
        for i in range(m):
            for j in range(n):
                if nums2[i] == nums1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    
                output = max(output,dp[i+1][j+1])
                
        return output
        