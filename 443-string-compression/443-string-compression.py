class Solution:
    def compress(self, chars: List[str]) -> int:
        def write(count,cur_index,i):
            if count == 1:
                chars[cur_index] = chars[i-1]
                cur_index += 1
                return (False,cur_index)
            else:
                chars[cur_index] = chars[i-1]
                cur_index += 1
                for ch in str(count):
                    chars[cur_index] = ch
                    cur_index += 1
            
            return (True,cur_index)
            
            
        if len(chars) == 1:
            return 1
        
        cur_index = 0
        count = 1
        i,size = 1,len(chars)
        
        while i < size:
            if chars[i] == chars[i-1]:
                count += 1
            else:
                res,cur_index = write(count,cur_index,i)
                if res:
                    count = 1
            
            i += 1
        
        res,cur_index = write(count,cur_index,i)
        # for _ in range(size - cur_index):
        #     chars.pop()
            
        return cur_index
            
                    
        
                    
        
        