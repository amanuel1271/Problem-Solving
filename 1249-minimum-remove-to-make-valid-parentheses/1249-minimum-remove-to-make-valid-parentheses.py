class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_pset = set()
        stack = deque([])
        maintain_bracket = []
        
        for index,ch in enumerate(s):
            if ch == '(' or ch == ')':
                maintain_bracket.append((ch,index))
                
        for ch,index in maintain_bracket:
            if ch == '(':
                stack.append((ch,index))
            elif ch == ')':
                if not stack:
                    remove_pset.add(index)
                    continue
                stack.pop()
                
        while stack:
            ch,i = stack.pop()
            remove_pset.add(i)
            
        ans = ''
        
        for i,ch in enumerate(s):
            if i not in remove_pset:
                ans += ch
                
        return ans
            
        
        
                
        