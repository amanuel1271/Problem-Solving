class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        l,r = 0,len(arr)-1
        ans = []
        arr.sort()
        median = arr[(len(arr)-1)//2]
        
        while l <= r and len(ans) < k:
            if abs(arr[r] - median) >= abs(arr[l]-median):
                ans.append(arr[r])
                r -= 1
            else:
                ans.append(arr[l])
                l += 1
                
        return ans
                
                