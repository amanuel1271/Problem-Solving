class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def dfs(i,stack,sequence_len):
            if i == len(num):
                return sequence_len >= 3
            if len(stack) <= 1:
                for j in range(i,len(num)):
                    stack.append(int(num[i:j+1]))
                    
                    if dfs(j+1,stack[:],sequence_len + 1):
                        return True
                    
                    stack.pop()
                    
                    if num[i] == '0':
                        break
                        
                return False
        
            top = stack.pop()
            bottom = stack.pop()
            for j in range(i,len(num)):
                summ = int(num[i:j+1])
                
                if summ == bottom + top:
                    stack.append(top)
                    stack.append(summ)
                    
                    if dfs(j+1,stack[:],sequence_len + 1):
                            return True
                        
                    stack.pop()
                    stack.pop()
                    
                if num[i] == '0':
                        break
                        
            return False
        
        return dfs(0,[],0)
            
            
            
            
            
            
            
        
        
        