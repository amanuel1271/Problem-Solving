class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        def backtrack(first):
            if len(curr) == k:  
                output.append(curr[:])
                return
                
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1)
                curr.pop()
        
        output = []
        backtrack(1)
        return output
        
            
            
            
        