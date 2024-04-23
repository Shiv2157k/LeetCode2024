from typing import List


class WordSearch:

    def exists(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: Backtrack
        T: O(N * 3 ^L)
        S: O(L)
        :param board:
        :param word:
        :return:
        """
        rows, cols = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def backtrack(row: int, col: int, pos: int):

            if pos == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[pos]:
                return False

            board[row][col] = '$'
            for direction in directions:
                dr = row + direction[0]
                dc = col + direction[1]
                result = backtrack(dr, dc, pos + 1)
                if result:
                    return result
            board[row][col] = word[pos]
            return result

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False
