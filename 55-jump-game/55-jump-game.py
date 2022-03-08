class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        store_bad_indice = dict()
        
        def dfs(i):
            if i == n-1:
                return True
            elif i > n-1:
                return False
            elif i in store_bad_indice:
                return False
            
            for j in range(1,nums[i] + 1):
                if i+j in store_bad_indice:
                    continue
                if dfs(i+j):
                    return True
                else:
                    store_bad_indice[i+j] = 0
            
            store_bad_indice[i] = 0
            return False
        
        return dfs(0)
            
            
        