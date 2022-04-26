class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        size_1,size_2,size_3 = len(s1),len(s2),len(s3)
        
        @lru_cache(None)
        def dfs(i,j,k):
            if i == size_1 and j == size_2 and k == size_3:
                return True
            
            if i < size_1 and k < size_3 and s3[k] == s1[i] and dfs(i+1,j,k+1):
                    return True
            if j < size_2 and k < size_3 and s3[k] == s2[j] and dfs(i,j+1,k+1):
                    return True
                
                
            return False
        
        return dfs(0,0,0)
            
            