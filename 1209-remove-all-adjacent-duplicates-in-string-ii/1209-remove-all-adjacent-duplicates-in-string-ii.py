class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        
        for ch in s:
            if not stack:
                stack.append([ch,1])
            else:
                if ch == stack[-1][0]:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([ch,1])
                    
        ans = ''
        while stack:
            ch,count = stack.pop()
            ans += ch * count
            
        return ans[::-1]