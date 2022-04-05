class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPre(word1,word2):
            size1,size2 = len(word1),len(word2)
            if size1 + 1 != size2:
                return False
            Q,Q_size = deque(),0
            for ch in word1:
                Q.append(ch)
                Q_size += 1
            
            for ch in word2:
                if Q_size == 0:
                    break
                if Q[0] == ch:
                    Q.popleft()
                    Q_size -= 1
            return Q_size == 0
        
        
        word_to_neighbors = defaultdict(list)
        words.sort(key = lambda word: len(word))
        size = len(words)
        
        for i in range(size):
            cur_word,size_ = words[i],len(words[i])
            for j in range(i+1,size):
                if len(words[j]) > size_ + 1:
                    break
                if isPre(cur_word,words[j]):
                    word_to_neighbors[cur_word].append(words[j])
                    
        self.ans = 1
        visited = set()
                
        
        @lru_cache(None)
        def dfs(ch):
            if len(word_to_neighbors[ch]) == 0:
                return 1
            
            ans = 0
            for neighbors in word_to_neighbors[ch]:
                visited.add(neighbors)
                ans = max(1 + dfs(neighbors),ans)
            
            return ans
                
        for word in words:
            if word not in visited:
                visited.add(word)
                self.ans = max(dfs(word),self.ans)
                
        return self.ans
                
        
        
            
                
                
                