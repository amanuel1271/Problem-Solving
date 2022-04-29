class Solution:
    def countVowelStrings(self, n: int) -> int:
        adj_list = {
            'a':['a','e','i','o','u'],
            'e': ['e','i','o','u'],
            'i': ['i','o','u'],
            'o': ['o','u'],
            'u': ['u']   
        }
        
        def generate(k):
            if k == 1:
                return ["a","e","i","o","u"]
            
            res = []
            for ch in generate(k-1):
                for nei in adj_list[ch[-1]]:
                    res.append(ch + nei)
            
            return res
        
        return len(generate(n))
                    
        