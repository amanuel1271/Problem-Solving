
class Solution:
        def minIncrementForUnique(self, arr: List[int]) -> int:
            arr.sort()
            n = len(arr)
            steps = 0
            for i in range(1,n):
                if arr[i] <= arr[i - 1]:
                    steps += (arr[i - 1] - arr[i] + 1)
                    arr[i] = arr[i - 1] + 1
            return steps
        
        
        