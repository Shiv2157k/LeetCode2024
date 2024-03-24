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
        curr = curr._is_word = True

    def searchWord(self, word: str) -> bool:

        def dfs(node: TrieNode, position: int=0):
            if position == len(word):
                return node.is_word

            if word[position] == ".":
                for next_node in node.children.values():
                    if dfs(next_node, position + 1):
                        return True
                return False
            if word[position] not in node.children:
                return False
            return dfs(node.children[word[position]], position + 1)

        return dfs(self._root)
