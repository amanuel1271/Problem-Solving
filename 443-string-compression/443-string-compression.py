class Solution:
    def compress(self, chars: List[str]) -> int:
        def write(count,cur_index,i):
            chars[cur_index] = chars[i-1]
            cur_index += 1
            if count == 1:
                return (False,cur_index)
            else:
                for ch in str(count):
                    chars[cur_index] = ch
                    cur_index += 1
            return (True,cur_index)
            
        cur_index,count,i,size = 0,1,1,len(chars)
        while i < size:
            if chars[i] == chars[i-1]:
                count += 1
            else:
                res,cur_index = write(count,cur_index,i)
                if res:
                    count = 1
            i += 1
        
        res,cur_index = write(count,cur_index,i)    
        return cur_index
            
                    
        
                    
        
        