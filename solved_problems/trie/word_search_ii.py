from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None
        self.is_visited = False


class WordSearch:

    def __init__(self):
        self._root = TrieNode()

    def find_words(self, board: List[List[int]], words: List[str]) -> List[str]:
        """
        Approach:
        T: O(M (4 * 3 ^L - 1))
        S: O(N)
        :param board:
        :param words:
        :return:
        """
        curr = self._root

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        words_matched = []

        # Step 1: Build the Trie Structure with words
        for word in words:
            curr = self._root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        def back_track(r: int, c: int, node: TrieNode):
            # hold the letter
            letter = board[r][c]
            # initialize the curr_node
            curr_node = node.children[letter]
            # base case
            # if we reached end of the word and it is not visited before
            # add it to the results and mark the visited as true
            if curr_node.word is not None and not curr_node.is_visited:
                words_matched.append(curr_node.word)
                curr_node.is_visited = True
            # mark the board with a delimiter until we explore all directions
            # from this grid
            board[r][c] = "$"

            # Explore all directions
            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]
                # if you have found the right next word keep back tracking
                if 0 <= dr < rows and 0 <= dc < cols and board[dr][dc] in curr_node.children:
                    back_track(dr, dc, curr_node)
            # reset the delimiter to the actual letter
            board[r][c] = letter
            # optimization by pruning once visited
            # if not curr_node.children:
            #     del curr_node.children[letter]

        # Step 2: Back Track if there is a letter in tries first most level
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in self._root.children:
                    back_track(row, col, self._root)
        return words_matched


if __name__ == "__main__":
    word_search = WordSearch()
    print(word_search.find_words(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ],
        ["oath", "pea", "eat", "rain", "neat", "oaaneateihkrvlfi"]
    ))
