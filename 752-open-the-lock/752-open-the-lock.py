class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set(deadends)
        s = {"0000"}
        Q = deque()
        
        if "0000" not in ends:
            Q.append(("0000",0))

        
        while Q:
            c,d = Q.popleft()
            if c == target:
                return d
                    
            for i in range(4):
                up,down = (int(c[i]) + 1) % 10, (int(c[i]) - 1) % 10
                nextl,nextr = c[:i] + str(down) + c[i + 1:], c[:i] + str(up) + c[i + 1:]
                if not(nextl in s) and not(nextl in ends):
                    Q.append((nextl,d + 1))
                    s.add(nextl)
                if not(nextr in s) and not (nextr in ends):
                    Q.append((nextr,d + 1))
                    s.add(nextr)        
        return -1
                
                
                
        
        
        
        
        