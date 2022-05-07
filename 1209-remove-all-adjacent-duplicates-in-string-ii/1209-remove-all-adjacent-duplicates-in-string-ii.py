class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        
        for ch in s:
            if not stack or ch != stack[-1][0]:
                stack.append([ch,1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

                    
        ans = ''
        while stack:
            ch,count = stack.pop()
            ans += ch * count
            
        return ans[::-1]