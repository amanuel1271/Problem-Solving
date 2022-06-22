class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = {}
        max_ = 0
        
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i]-arr[j] < arr[j] and (arr[i]-arr[j],arr[j]) in dp:
                    dp[(arr[j],arr[i])] = dp[(arr[i]-arr[j],arr[j])] + 1
                    max_ = max(max_,dp[(arr[j],arr[i])])
                else:
                    dp[(arr[j],arr[i])] = 2
                    
        return max_ if max_ >= 3 else 0