from typing import Optional


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.__root = TrieNode()

    def add_word(self, word: str) -> None:
        curr = self.__root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:

        def depth_first_search(curr: Optional[TrieNode], ptr: int) -> bool:

            if ptr == len(word):
                return True

            if word[ptr] == '.':
                for children in curr.children.values():
                    if depth_first_search(children, ptr + 1):
                        return True
                return False
            if word[ptr] not in curr.children:
                return False
            return depth_first_search(curr.children[word[ptr]], ptr + 1)

        return depth_first_search(self.__root, 0)
