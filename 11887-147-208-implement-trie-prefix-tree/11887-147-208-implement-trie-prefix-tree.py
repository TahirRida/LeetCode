class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c]=TrieNode() 
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        