class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_symbol = {
            1: 'I',4: 'IV' ,5: 'V',9: 'IX',10: 'X',40: 'XL',50:'L',90:'XC',100:'C',400:'CD',500: 'D',900:'CM',1000:'M'
        }
        
        def find_str(val):
            if val >= 1000:
                return 'M',1000
            
            prev = 1
            for values in value_to_symbol:
                if val == values:
                    return value_to_symbol[val],val
                elif values > val:
                    return value_to_symbol[prev],prev
                prev = values
                
            return value_to_symbol[prev],prev
        
        ans = ''
        while num != 0:
            ch,deduct_amt = find_str(num)
            ans += ch
            num -= deduct_amt
            
        return ans
            
        