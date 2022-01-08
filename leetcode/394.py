class Solution:
    def decodeString(self, s):
        stk, ans, n = deque(), "", ""
        for c in s:
            if c.isalpha():   
                ans += c
            elif c.isdigit(): 
                n += c
            elif c == '[': 
                stk.append((n, ans))
                n, ans = "", ""
            else:
                cnt, prev = stk.pop()
                ans = prev + ans * int(cnt)
        return ans
