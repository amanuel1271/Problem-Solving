class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        cnt = 0
        for i in range(len(arr)-1):
            a = 0
            for j in range(i+1,len(arr)):
                a ^= arr[j-1]
                b = 0
                for k in range(j,len(arr)):
                    b ^= arr[k]
                    if a == b:
                        cnt += 1
                        
        return cnt
                
        