from typing import List
from pprint import pprint


class Matrix:

    def set_to_zeroes_v1(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: In Place
        T: O(M*N)
        S: O(1)
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        is_col = False

        for row in range(rows):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        if is_col:
            for row in range(rows):
                matrix[row][0] = 0

        return matrix

    def set_to_zeroes_v0(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Using Visited Sets
        T: O(M*N)
        S: O(M + N)
        :param matrix:
        :return:
        """
        row_set, col_set = set(), set()

        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0
        return matrix


if __name__ == "__main__":
    matrix = Matrix()
    pprint(matrix.set_to_zeroes_v0(
        [
            [1, 1, 1], [1, 0, 1], [1, 1, 1]
        ]
    ))
    pprint(matrix.set_to_zeroes_v1(
        [
            [1, 1, 1], [1, 0, 1], [1, 1, 1]
        ]
    ))

    pprint(matrix.set_to_zeroes_v0(
        [
            [0, 2, 3, 4], [9, 7, 0, 8], [1, 1, 1, 1]
        ]
    ))
    pprint(matrix.set_to_zeroes_v1(
        [
            [0, 2, 3, 4],
            [9, 7, 0, 8],
            [1, 1, 1, 1]
        ]
    ))