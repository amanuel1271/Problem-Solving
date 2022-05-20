class TrieNode:
    def __init__(self):
        self.terminal = False
        self.nextnodes = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ch_to_index = {}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            self.ch_to_index[letter] = ord(letter) - ord('a')
        
    def insert(self, word: str) -> None:
        tmp = self.root
        for ch in word:
            index = self.ch_to_index[ch]
            if tmp.nextnodes[index] is None:
                tmp.nextnodes[index] = TrieNode()
            tmp = tmp.nextnodes[index]   
        tmp.terminal = True

        
    def search(self, word: str) -> bool:
        tmp = self.root
        for ch in word:
            index = self.ch_to_index[ch]
            if tmp.nextnodes[index] is None:
                return False
            tmp = tmp.nextnodes[index]  
        return tmp.terminal
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for ch in prefix:
            index = self.ch_to_index[ch]
            if tmp.nextnodes[index] is None:
                return False
            tmp = tmp.nextnodes[index]      
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)