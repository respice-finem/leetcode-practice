class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)

    def dfs(self, curr, word):
        if len(word) == 0:
            return curr.isEnd
        if word[0] != '.' and not curr.children.get(word[0], None):
            return False

        output = False
        for e in curr.children:
            if word[0] == '.':
                output = self.dfs(curr.children[e], word[1:])
            if word[0] == e:
                output = self.dfs(curr.children[e], word[1:])
            if output:
                return True
        return output