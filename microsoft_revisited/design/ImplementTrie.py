class TrieNode:

    def __init__(self, char=''):
        self.children = {}
        self.char = char
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        T: O(M)
        S: O(M)
        :param word:
        :return:
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        """
        T: O(M)
        S: O(1)
        :param word:
        :return:
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        T: O(M)
        S: O(1)
        :param prefix:
        :return:
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
