from typing import List


class WordSearch:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: Backtracking
        T: O(N * 3^L)
        S: O(L)
        :param board:
        :param word:
        :return:
        """
        def backtrack(r: int, c: int, pos: int):

            if pos == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[pos]:
                return False
            board[r][c] = '$'
            result = False

            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]

                result = backtrack(dr, dc, pos + 1)
                if result:
                    return result
            board[r][c] = word[pos]
            return result

        rows, cols = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False
