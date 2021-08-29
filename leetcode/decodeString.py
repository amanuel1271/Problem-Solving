class Solution:
    def decodeString(self, s: str) -> str:
        i,final_string= 0,''
        
        while i < len(s):
            while i < len(s) and not s[i].isdigit():
                final_string += s[i]
                i += 1

            if i == len(s):
                break
                
            num_str = ''
            while s[i] != "[":
                num_str += s[i]
                i += 1
                
            recurse_string =  ''
            num = int(num_str)
            i += 1
            bracket_list_ = []
            
            while i < len(s) and (s[i] != ']' or bracket_list_):
                recurse_string += s[i]
                if s[i] == "[":
                    bracket_list_.append('[')
                if s[i] == ']' and bracket_list_:
                    bracket_list_.pop(0)
                i += 1
    
            final_string += num * self.decodeString(recurse_string)
            i += 1
        
        return final_string
