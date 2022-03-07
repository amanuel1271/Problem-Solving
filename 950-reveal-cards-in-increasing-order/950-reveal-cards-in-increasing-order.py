class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        size,ans = len(deck),[]
        i = size - 1
        
        deck.sort()
        
        while i >= 0:
            if ans:
                ans = [deck[i]] + [ans.pop()] + ans 
            else:
                ans.append(deck[i]) 
            i -= 1
                
        return ans
                
        
        
        