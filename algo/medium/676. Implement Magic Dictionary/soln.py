class MagicDictionary:

    def __init__(self):
        self.magic_dict = {}

    def buildDict(self, dictionary: List[str]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)

        TODO:
        1. Since it is dependent on the location where the index is changed, we just keep track of distinct words
        """
        for word in dictionary:
            if len(word) not in self.magic_dict:
                self.magic_dict[len(word)] = [word]
            else:
                self.magic_dict[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        TODO:
        1. Check if same length, if same length, get the diff between two strings at the same index
        """
        for word in self.magic_dict.get(len(searchWord), []):
            ct = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    ct += 1
                if ct > 1:
                    break
            if ct == 1:
                return True

        return False