class Solution:
    def canCross(self, stones: List[int]) -> bool:
        size = len(stones)
        if stones[1] > 1:
            return False
        
        def binary_search(arr,target):
            l,size = 0,len(arr)
            r = size - 1
            
            while l <= r:
                mid = (l+r)//2
                if arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return -1
        
                
            
        @lru_cache(None)
        def cross(i,last_jump):
            if i == size - 1:
                return True
        
            
            for option in [last_jump-1,last_jump,last_jump+1]:
                if option >= 1:
                    target = option + stones[i]
                    search_i = binary_search(stones[i+1:],target)
                    if search_i == -1:
                        continue

                    if cross(i + search_i + 1,option):
                        return True
                
            return False
        
        return cross(0,0)
                
            
            
        