class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.ans = []
        
        def dfs(target, path, factor):
            if len(path) > 0:
                self.ans.append(path + [target])
            
            for i in range(factor, int(sqrt(target)) + 1):
                if target % i == 0:
                    dfs(target // i, path + [i], i)
                
        dfs(n, [], 2)
        return self.ans
        
        
        
        
        