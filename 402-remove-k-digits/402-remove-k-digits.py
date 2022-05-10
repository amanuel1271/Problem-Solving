class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for ch in num:
            while stack and ch < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            if stack or ch != '0':
                stack.append(ch)
            
        final_stack = stack[:-k] if k else stack
        res = ''.join(final_stack)#.lstrip('0')
        return res if res != '' else '0'
                
        