from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.isVisited = False
        self.word = None


class WordSearchII:

    def __init__(self):
        self._root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Step 1: Build the trie of words
        for word in words:
            curr = self._root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        # Step 2: DFS on the board
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        results = []

        def backtrack(r, c, node):
            letter = board[r][c]
            currNode = node.children[letter]

            if currNode.word and not currNode.isVisited:
                results.append(currNode.children)
                currNode.isVisited = True

            board[r][c] = '$'

            for direction in directions:
                dr = r + direction[0]
                dc = c + directions[1]

                if 0 <= dr < rows and 0 <= dc < cols and board[dr][dc] in currNode.children:
                    backtrack(dr, dc, currNode)
            board[r][c] = letter

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in self._root.children:
                    backtrack(row, col, self._root)
        return results

