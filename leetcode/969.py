class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        index_to_put = len(arr) - 1
        res = []
        
        while index_to_put != 0:
            maxIndex = arr.index(max(arr[:index_to_put + 1]))
            if maxIndex != 0:
                arr = list(reversed(arr[:maxIndex + 1]))+ arr[maxIndex + 1:]
                res.append(maxIndex + 1)
            else:
                arr = list(reversed(arr[:index_to_put + 1]))+ arr[index_to_put + 1:]
                res.append(index_to_put + 1)
                index_to_put -= 1
        
        
            
        return res
