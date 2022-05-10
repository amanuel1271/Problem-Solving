class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.stack_size = 1
        self.index = 0
        
        

    def visit(self, url: str) -> None:
        while self.stack_size  > self.index + 1:
            self.stack.pop()
            self.stack_size -= 1
        
        self.stack.append(url)
        self.index += 1
        self.stack_size += 1
        

    def back(self, steps: int) -> str:
        self.index = max(self.index - steps,0)
        return self.stack[self.index]
        
            
    def forward(self, steps: int) -> str:
        self.index = min(self.stack_size - 1,self.index + steps)
        return self.stack[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)