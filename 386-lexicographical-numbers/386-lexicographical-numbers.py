class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [1]

        while len(result) < n:
            toAdd = result[-1] * 10

            while toAdd > n:
                toAdd /= 10
                toAdd += 1

                while int(toAdd) % 10 == 0:
                    toAdd /= 10
            result.append(int(toAdd))
        return result
                
            
            
        