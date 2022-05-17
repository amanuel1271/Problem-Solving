class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def helper(num):
            if num%3 == 0 and num%5 == 0:
                return "FizzBuzz"
            elif num%3 == 0:
                return "Fizz"
            elif num%5 == 0:
                return "Buzz"
            return str(num)
        
        return [helper(i) for i in range(1,n+1)]
    
        