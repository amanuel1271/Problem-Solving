class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        len_ = len(arr)
        if len_ <= 2:
            return False
        

        i = arr.index(max(arr))
        if i == 0 or i == len_ - 1:
            return False
        
        for j in range(len_):
            if (1 <= j <= i and arr[j] <= arr[j-1]) or (j >= i + 1 and arr[j] >= arr[j-1]):
                    return False
        return True
        
        
            
        