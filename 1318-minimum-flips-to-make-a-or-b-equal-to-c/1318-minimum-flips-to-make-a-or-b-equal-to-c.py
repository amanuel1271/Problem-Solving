class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def convert_to_bin(num):
            return '{:032b}'.format(num)
        
        BIT_SIZE = 32
        operand1,operand2,result = convert_to_bin(a),convert_to_bin(b),convert_to_bin(c)
        cnt = 0
        
        for i in range(BIT_SIZE):
            if result[i] == '0':
                add_1 = 1 if operand1[i] == '1' else 0
                add_2 = 1 if operand2[i] == '1' else 0
                cnt += add_1 + add_2
            else:
                add = 1 if operand1[i] == '0' and operand2[i] == '0' else 0
                cnt += add
                
        return cnt
                