class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        return self.dfs(node, word)
    
    def dfs(self, node, word):
        if not word:
            return node.isWord
            
        if word[0] == ".":
            for n in node.children.values():
                if self.dfs(n, word[1:]):
                    return True
        else:
            node = node.children.get(word[0])
            if not node:
                return False
            return self.dfs(node, word[1:])