from typing import List



class SetMatrixZeroes:


    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        Approach: Simulation
        T: O(MN)
        S: O(1)
        :param matrix:
        :return:
        """

        rows = len(matrix)
        cols = len(matrix[0])
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
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(1, cols):
                matrix[0][col] = 0

        if is_col:
            for row in range(rows):
                matrix[row][0] = 0
