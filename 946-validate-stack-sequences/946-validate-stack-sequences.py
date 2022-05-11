class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        size = len(pushed)
        push_i,pop_j = 0,0
        
        while push_i < size or pop_j < size:
            if stack and stack[-1] == popped[pop_j]:
                stack.pop()
                pop_j += 1
            elif push_i < size:
                stack.append(pushed[push_i])
                push_i += 1
            else:
                return False
            
        return True
            
        
        