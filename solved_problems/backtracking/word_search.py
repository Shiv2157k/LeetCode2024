from typing import List


class Word:

    def search_in_board(self, board: List[List[int]], word: str) -> bool:
        """
        Approach: Back Tracking
        T: O()
        S: O(W)
        :param board:
        :param word:
        :return:
        """

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def backtrack(row: int, col: int, suffix: str):

            # base case
            if len(suffix) == 0:
                return True
            if row < 0 or row == rows or col < 0 or col == cols or board[row][col] != suffix[0]:
                return False

            result = False
            board[row][col] = '$'
            for direction in directions:
                dr = row + direction[0]
                dc = col + direction[1]
                result = backtrack(dr, dc, suffix[1:])
                if result:
                    break
            board[row][col] = suffix[0]
            return result

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, word):
                        return True
        return False


if __name__ == "__main__":
    word = Word()
    print(word.search_in_board(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCCED"
    ))
    print(word.search_in_board(
        [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        "SEE"
    ))
    print(word.search_in_board(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCD"
    ))
