class Solution:
    def canCross(self, stones: List[int]) -> bool:
        size = len(stones)
        if stones[1] > 1:
            return False
        
        store_ind = {}
        for i in range(len(stones)):
            store_ind[stones[i]] = i
        
                
            
        @lru_cache(None)
        def cross(i,last_jump):
            if i == size - 1:
                return True
        
            
            for option in [last_jump-1,last_jump,last_jump+1]:
                if option >= 1:
                    target = option + stones[i]
                    if target in store_ind:
                        indice = store_ind[target]
                    else:
                        continue
                    if cross(indice,option):
                        return True
                
            return False
        
        return cross(0,0)
                
            
            
        