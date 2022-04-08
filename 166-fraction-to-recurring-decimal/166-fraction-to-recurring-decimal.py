class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        
        is_neg = False
        if (numerator < 0 or denominator < 0) and not(numerator < 0 and denominator < 0):
            is_neg = True
            
        numerator,denominator = abs(numerator),abs(denominator)
        if is_neg:
            integer_portion = '-' + str(numerator//denominator)
        else:
            integer_portion = str(numerator//denominator)

        
        fraction_part = '.'
        rem_to_ch = {}
        prev = numerator//denominator
        sub_from = numerator - (prev * denominator)
        sub_from *= 10
        repeated_start_char,index,save_index = None,0,0
        

        while sub_from != 0:
            if sub_from in rem_to_ch:
                repeated_start_char = str(sub_from//denominator)
                save_index = rem_to_ch[sub_from][1]
                break
            else:
                rem_to_ch[sub_from] = (str(sub_from//denominator),index)
                
            index += 1

            fraction_part += str(sub_from//denominator)
            prev = sub_from//denominator
            sub_from = (sub_from - (prev * denominator)) * 10
            
        if fraction_part == '.':
            return integer_portion
        elif repeated_start_char is None:
            return integer_portion + fraction_part
        
        return_str,i = '.',0
        for ch in fraction_part[1:]:
            if ch == repeated_start_char and i == save_index:
                return_str += '(' + ch
            else:
                return_str += ch
            
            i += 1
                
        return integer_portion + return_str + ')'
        

        
        
        
        