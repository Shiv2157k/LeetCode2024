from typing import List


class Square:

    def maximal_area_in_matrix_v1(self, matrix: List[List[str]]):
        """
        Approach: DP Space Optimized
        T: O(MN)
        S: O(N)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        prev = length = 0
        dp = [0] * (cols + 1)

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                temp = dp[col]
                if matrix[row - 1][col - 1] == "1":
                    dp[col] = 1 + min(prev, dp[col - 1], dp[col])
                    length = max(length, dp[col])
                else:
                    dp[col] = 0
                prev = temp
        return length * length

    def maximal_area_in_matrix_v0(self, matrix: List[List[int]]):
        """
        Approach: DP
        Time Complexity: O(MN)
        Space Complexity: O(MN
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        length = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if matrix[row - 1][col - 1] == "1":
                    dp[row][col] = 1 + min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1])
                    length = max(length, dp[row][col])
        return length * length


if __name__ == "__main__":
    square = Square()
    print(square.maximal_area_in_matrix_v0(
        [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "0", "0"],
            ["1", "1", "1", "1", "1"],
        ]
    ))
    print(square.maximal_area_in_matrix_v1(
        [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "1"],
        ]
    ))
    print(square.maximal_area_in_matrix_v0(
        [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "1"],
        ]
    ))
    print(square.maximal_area_in_matrix_v1(
        [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "1"],
        ]
    ))

    print(square.maximal_area_in_matrix_v0(
        [
            ["1", "1"],
            ["1", "0"]
        ]
    ))
    print(square.maximal_area_in_matrix_v1(
        [
            ["1", "1"],
            ["1", "0"]
        ]
    ))
    print(square.maximal_area_in_matrix_v0(
        [["1", "1"]]
    ))
    print(square.maximal_area_in_matrix_v1(
        [["1", "1"]]
    ))
    print(square.maximal_area_in_matrix_v0(
        [["1"], ["1"]]
    ))
    print(square.maximal_area_in_matrix_v1(
        [["1"], ["1"]]
    ))
