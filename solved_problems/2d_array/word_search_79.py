from typing import List


class WordSearch:

    def search(self, board: List[List[int]], word: str) -> bool:
        """
        Approach: BackTracking
        T: O(N * 3 ^ L)
        S: O(L)
        :param board:
        :return:
        """
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def back_track(r: int, c: int, suffix: str) -> bool:

            if len(suffix) == 0:
                return True
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != suffix[0]:
                return False

            # mark the board from re visiting
            board[r][c] = "$"
            result = False
            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]
                result = back_track(dr, dc, suffix[1:])
                if result:
                    break
            board[r][c] = suffix[0]
            return result

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if back_track(row, col, word):
                        return True
        return False


if __name__ == "__main__":
    wordSearch = WordSearch()
    print(wordSearch.search(
    [
            ["A", "B", "P", "E"],
            ["S", "F", "A", "S"],
            ["A", "A", "P", "E"]
        ], "PAPA"
    ))
