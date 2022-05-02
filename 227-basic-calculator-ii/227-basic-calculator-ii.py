class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        list_rep = list(s)
        operator_list = list(filter(lambda ch: ch in '*/+-',list_rep))
        replace = (((s.replace("+"," ")).replace("-"," ")).replace('*'," ")).replace('/'," ")
        operand_list =  replace.split()
        op_dic = {'+': lambda x,y : int(x) + int(y),
                 '-': lambda x,y : int(x) - int(y),
                 '*': lambda x,y : int(x) * int(y),
                 '/': lambda x,y : int(x) // int(y)}
        
        def op_precedence(pre_str,size):
            i,ptr = 0,0
            while ptr < size:
                if operator_list[i] in pre_str:
                    res = op_dic[operator_list[i]](operand_list[i],operand_list[i+1])
                    operator_list.pop(i)
                    operand_list[i] = str(res)
                    operand_list.pop(i+1)
                else:
                    i += 1  
                ptr += 1
            
        
        
        op_precedence('*/',len(operator_list))
        op_precedence('+-',len(operator_list))
        #print(operand_list)
        
        return int(operand_list[0])
            
            
        
        