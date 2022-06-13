class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        last,ans = 0,0
        
        for num,per in brackets:
            amt = max(min(income,num) - last,0)
            ans += amt * (per/100)
            last = num
            
        return ans
        
            
        