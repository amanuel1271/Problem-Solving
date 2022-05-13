class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = 1
        

    def next(self, price: int) -> int:
        ans = [price,self.index]
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
            
        res = ans[1] - self.stack[-1][1] if self.stack else ans[1]
        self.index += 1
        self.stack.append(ans) 
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)