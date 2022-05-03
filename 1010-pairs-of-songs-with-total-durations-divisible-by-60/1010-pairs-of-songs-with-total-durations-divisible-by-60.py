class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        store = [0]*121
        count = 0
        
        for t in time:
            count += store[60-(t%60)]
            count += store[120-(t%60)]
            if t%60 == 0:
                count += store[0]
            store[t%60] = store[t%60] + 1   
        return count