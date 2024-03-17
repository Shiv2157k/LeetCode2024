from typing import List


class Matrix:

    def found_target_v1(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Pruning or Search Space Reduction
        T: O(N)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        length, width = len(matrix), len(matrix[0])

        row = length - 1
        col = 0

        while row >= 0 and col < width:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False

    def binary_search(self, matrix: List[List[int]], target: int, start: int, is_vertical: int) -> bool:
        """
        :param matrix:
        :param target:
        :param start:
        :param is_vertical:
        :return:
        """
        low = start
        high = len(matrix) - 1 if is_vertical else len(matrix[0]) - 1

        while high >= low:

            mid = low + (high - low) // 2
            if not is_vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True
        return False

    def found_target_v0(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Binary Search
        T: O(log(N!)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False

        for index in range(min(len(matrix), len(matrix[0]))):

            vertical_found = self.binary_search(matrix, target, index, True)
            horizontal_found = self.binary_search(matrix, target, index, False)

            if vertical_found or horizontal_found:
                return True
        return False


if __name__ == "__main__":
    matrix = Matrix()
    print(matrix.found_target_v0(
        [
            [5, 9, 12, 13, 27],
            [7, 11, 19, 23, 28],
            [8, 15, 20, 24, 29],
            [6, 16, 21, 25, 30]
        ], 19
    ))
    print(matrix.found_target_v1(
        [
            [5, 9, 12, 13, 27],
            [7, 11, 19, 23, 28],
            [8, 15, 20, 24, 29],
            [6, 16, 21, 25, 30]
        ], 19
    ))
    print(matrix.found_target_v0(
        [
            [5, 9, 12, 13, 27],
            [7, 11, 19, 23, 28],
            [8, 15, 20, 24, 29],
            [6, 16, 21, 25, 30]
        ], 99
    ))
    print(matrix.found_target_v1(
        [
            [5, 9, 12, 13, 27],
            [7, 11, 19, 23, 28],
            [8, 15, 20, 24, 29],
            [6, 16, 21, 25, 30]
        ], 99
    ))