class StockSpanner:

    def __init__(self):
        self.stack = [[-math.inf,-1]]
        self.index = 0
        

    def next(self, price: int) -> int:
        ans = [price,self.index]
        while self.stack and self.stack[-1][0] != -math.inf and self.stack[-1][0] <= price:
            self.stack.pop()
        
        res = ans[1] - self.stack[-1][1]
        self.stack.append(ans) 
        self.index += 1
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)