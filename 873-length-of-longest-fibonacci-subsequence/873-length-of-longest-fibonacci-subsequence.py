class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = {}
        maxx = 0
        
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i]-arr[j] < arr[j] and (arr[i]-arr[j],arr[j]) in dp:
                    dp[(arr[j],arr[i])] = dp[(arr[i]-arr[j],arr[j])] + 1
                    maxx = max(maxx,dp[(arr[j],arr[i])])
                else:
                    dp[(arr[j],arr[i])] = 2
                    
        return maxx if maxx >= 3 else 0