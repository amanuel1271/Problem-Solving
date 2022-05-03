class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        store = {}
        count = 0
        
        for t in time:
            if 60-(t%60) in store:
                count += store[60-(t%60)]
            if 120-(t%60) in store:
                count += store[120-(t%60)]
            if t%60 == 0 and 0 in store:
                count += store[0]
            
            store[t%60] = store.get(t%60,0) + 1
            
        return count