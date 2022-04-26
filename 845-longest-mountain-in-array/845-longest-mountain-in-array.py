class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        start,end,peak = 0,0,0
        size = len(arr)
        
        while start < size - 1:
            if arr[start + 1] > arr[start]:
                peak = start + 1
                while peak < size-1 and  arr[peak+1] > arr[peak]:
                    peak += 1
                    
                if peak < size-1:
                    end = peak
                    if end == size - 1 or arr[end + 1] == arr[end]:
                        start = end +1
                        continue
                    while end < size - 1 and arr[end + 1] < arr[end]:
                        end += 1
                        
                    res = max(res,end-start + 1)
                    start = end
                else:
                    start = peak + 1     
            else:
                start += 1
                
        return res
                
        
                
                
        
        