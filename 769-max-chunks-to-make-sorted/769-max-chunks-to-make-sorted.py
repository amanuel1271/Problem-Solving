class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunkCount,expectedSum,currSum = 0,0,0
        
        for i in range(len(arr)):
            expectedSum += i
            currSum += arr[i]
            
            if expectedSum == currSum:
                chunkCount += 1

                
        return chunkCount
            
        