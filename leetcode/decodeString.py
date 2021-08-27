class Solution:
    def decodeString(self, s: str) -> str:
        i,final_string= 0,''
        
        while i < len(s):
            while i < len(s) and not s[i].isdigit():
                final_string += s[i]
                i += 1

            if i == len(s):
                break
                
            num_st = ''
            while s[i] != "[":
                num_st += s[i]
                i += 1
                
            recurse_string =  ''
            num = int(num_st)
            i += 1
            list_ = []
            
            while i < len(s) and (s[i] != ']' or list_):
                recurse_string += s[i]
                if s[i] == "[":
                    list_.append('[')
                if s[i] == ']' and list_:
                    list_.pop(0)
                i += 1
    
            final_string += num * self.decodeString(recurse_string)
            i += 1
        
        return final_string
