class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.acc = []
        def helper(mod_str,opening,closing):
            
            if closing == n:
                self.acc.append(mod_str)
                return
            
            elif closing < opening:
                helper(mod_str + ')',opening,closing + 1)
            if opening < n:
                helper(mod_str + '(',opening + 1,closing)
                
            
        
        helper('',0,0)       
        return self.acc
    