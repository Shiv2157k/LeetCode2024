from typing import Optional


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self._root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self._root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(curr: Optional[TrieNode], ptr: int):

            if ptr == len(word):
                return curr.is_word

            if word[ptr] == ".":
                for children in curr.children.values():
                    if dfs(children, ptr + 1):
                        return True
                return False
            if word[ptr] not in curr.children:
                return False
            return dfs(curr.children[word[ptr]], ptr + 1)

        return dfs(self._root, 0)
