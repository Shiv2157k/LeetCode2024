
# leet code 208 implement later

class TrieNode:

    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self._root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
                curr = curr.children[char]
            else:
                curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self._root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self._root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True




