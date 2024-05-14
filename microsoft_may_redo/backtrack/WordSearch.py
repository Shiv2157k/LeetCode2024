from typing import List


class WordSearch:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: Back Track
        T: O(N * 3^L)
        S: O(L)
        :param board:
        :param word:
        :return:
        """

        rows = len(board)
        cols = len(board[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def backtrack(r: int, c: int, pos: int):
            # base cases
            if pos == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[pos]:
                return False

            result = False
            # mark to limit cycle
            board[r][c] = '$'

            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]

                result = backtrack(dr, dc, pos)
                if result:
                    return result
            board[r][c] = word[pos]
            return result

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False
