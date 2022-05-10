class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        count = collections.Counter(s)
        stack = []
        
        for ch in s:
            if ch in visited:
                count[ch] -= 1
                continue
                
            while stack and ch < stack[-1] and count[stack[-1]] > 1:
                count[stack[-1]] -= 1
                visited.remove(stack.pop())
            

            stack.append(ch)
            visited.add(ch)
                
        
        return ''.join(stack)
        