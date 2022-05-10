class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for ch in num:
            while stack and int(ch) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
                
            stack.append(ch)
            
        res = stack[:-k] if k else stack
        return '0' if not res else str(int(''.join(res)))
                
        