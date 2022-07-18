
        
def insertAndUpdate(memo,word):
    pre = ''
    for ch in word:
        pre += ch
        prevSuggestions = memo.get(pre,[])
        memo[pre] = sorted(prevSuggestions + [word])[:3]
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        memo = dict()
        for word in products:
            insertAndUpdate(memo,word)
            
        pre,ans = '',[]
        for ch in searchWord:
            pre += ch
            ans.append(memo.get(pre,[]))
            
        return ans
            
        