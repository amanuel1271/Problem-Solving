class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process(string):
            size = len(string)
            ptr,i = 0,0
            
            while ptr < size:
                if string[i] != '#':
                    i += 1
                else:
                    string.pop(i)
                    if i > 0:
                        string.pop(i-1)
                        i -= 1
                ptr += 1
                
            return ''.join(string)
            
            
        return process(list(s)) == process(list(t))