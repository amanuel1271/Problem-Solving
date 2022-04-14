class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [poured]
        
        
        for _ in range(query_row):
            size = len(glasses)
            temp = [0 for _ in range(size + 1)]
            for i in range(size):
                pour = (glasses[i] - 1) / 2
                if pour > 0:
                    temp[i],temp[i+1] = temp[i] + pour,temp[i+1] + pour
                    
            glasses = temp
            
        return min(float(1),float(glasses[query_glass]))
                    
        
        
        
            
        
        
        