from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None
        self.is_visited = False


class WordBreakII:

    def __init__(self):
        self.__root = TrieNode()

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Approach: Back Track and Trie
        T: O(M (4 * 3 ^ (L - 1)))
        S: O(N)
        :param board:
        :param words:
        :return:
        """
        curr = self.__root

        for word in words:
            curr = self.__root
            for letter in word:
                curr.children[letter] = curr.children.get(letter, TrieNode())
                curr = curr.children[letter]
            curr.word = word

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        rows = len(board)
        cols = len(board[0])
        result = []

        def backtrack(r: int, c: int, node: TrieNode):

            letter = board[r][c]

            curr_node = node.children[letter]
            # base case
            if curr.word is not None and not curr.is_visited:
                result.append(curr.word)
                curr.word = None
                curr.is_visited = True
            board[r][c] = '$'

            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]

                if 0 <= dr < rows and 0 <= dc < cols and board[dr][dc] in curr_node.children:
                    backtrack(dr, dc, curr_node)
            board[r][c] = letter

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in self.__root.children:
                    backtrack(row, col, self.__root)
        return result
