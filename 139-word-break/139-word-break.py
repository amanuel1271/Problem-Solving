class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        preprocess = defaultdict(list)
        for words in wordDict:
            preprocess[words[0]].append(words)
        

        
        @lru_cache(None)
        def dp(word):
            if word == '':
                return True
            
            for words in preprocess[word[0]]:
                cut_len = len(words)
                if cut_len <= len(word) and word[:cut_len] == words:
                    if dp(word[cut_len:]):
                        return True
            return False
        
        return dp(s)
            
            
            