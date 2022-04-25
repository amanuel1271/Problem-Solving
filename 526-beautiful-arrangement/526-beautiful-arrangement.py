class Solution:
    def countArrangement(self, n: int) -> int:
        S = {i for i in range(1,n+1)}
        self.ans = 0
        
        def backtrack(N, S):
            if N > n:
                self.ans += 1
                return
            
            for i in S:
                if N%i == 0 or i%N == 0:
                    backtrack(N+1, S-{i})
                    
        backtrack(1, S)
        return self.ans
            
        