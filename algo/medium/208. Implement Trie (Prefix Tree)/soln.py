class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return True