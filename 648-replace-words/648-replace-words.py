class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        tmp = self.root
        for ch in word:
            if ch not in tmp.children:
                tmp.children[ch] = TrieNode()
            tmp = tmp.children[ch]     
        tmp.end = True
        
    def search(self,word):
        tmp = self.root
        for i,ch in enumerate(word):
            if ch in tmp.children:
                if tmp.children[ch].end:
                    return word[:i+1]
                tmp = tmp.children[ch]
            else:
                break
                
        return word # if no root found return the whole word
            


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
            
        sentence_lst = sentence.split()
        return ' '.join(list(map(lambda word: trie.search(word),sentence_lst)))
        