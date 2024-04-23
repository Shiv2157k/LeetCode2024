from typing import List, Tuple, Dict


class TrieNode:

    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.word: str = None
        self.is_visited: bool = False


class WordSearchII:

    def __init__(self):
        self._root = TrieNode()

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Step 1: build the trie out of words
        for word in words:
            curr = self._root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        # step 2: Explore all words from the board through dfs
        rows: int = len(board)
        cols: int = len(board[0])
        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        results: List[str] = []

        def backtrack(r: int, c: int, node: TrieNode):
            letter = board[r][c]

            curr_node = node.children[letter]

            if curr_node.word is not None and not curr_node.is_visited:
                results.append(curr_node.word)
                curr_node.word = None
                curr_node.is_visited = True

            board[r][c] = '$'

            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]

                if 0 <= dr < rows and 0 <= dc < cols and board[dr][dc] in curr_node.children:
                    backtrack(dr, dc, curr_node)
            board[r][c] = letter

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in self._root.children:
                    backtrack(row, col, self._root)
        return results
