class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operatorstack = deque()
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b 
        }
        
        #functional python, you can use lambda
        
        for i,op in enumerate(tokens):
            if op in '+*-/':
                operand2 = operatorstack.pop()
                operand1 = operatorstack.pop()
                res = operations[op](int(operand1),int(operand2))
                operatorstack.append(str(res))
            else:
                operatorstack.append(op)
                
        return int(operatorstack.pop())
            
