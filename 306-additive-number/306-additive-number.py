class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        
        def dfs(i,stack,sequence_len):
            if i == len(num):
                return sequence_len >= 3
            if len(stack) <= 1:
                if num[i] == '0':
                    stack.append(0)
                    return dfs(i+1,stack,sequence_len + 1)
                for j in range(i,len(num)):
                    stack.append(int(num[i:j+1]))
                    if dfs(j+1,stack[:],sequence_len + 1):
                        return True
                    stack.pop()
                return False
        
            top = stack.pop()
            bottom = stack.pop()
            if num[i] == '0':
                if bottom + top == 0:
                    stack.append(0)
                    stack.append(0)
                    return dfs(i+1,stack,sequence_len+1)
                stack.append(bottom)
                stack.append(top)
                return False
            
            for j in range(i,len(num)):
                summ = int(num[i:j+1])
                if summ == bottom + top:
                    stack.append(top)
                    stack.append(summ)
                    if dfs(j+1,stack[:],sequence_len + 1):
                            return True
                    stack.pop()
                    stack.pop()
            return False
        
        return dfs(0,[],0)
            
            
            
            
            
            
            
        
        
        