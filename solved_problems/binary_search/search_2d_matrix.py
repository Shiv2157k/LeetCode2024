from typing import List


class TwoDimensionalMatrix:


    def search_matrix_v1(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Binary Search
        T: O(log(m,n))
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            return False

        left, right = 0, rows * cols - 1

        while left <= right:
            pivot_index = left + (right - left) // 2
            pivot_element = matrix[pivot_index // cols][pivot_index % cols]

            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_index - 1
                else:
                    left = pivot_index + 1
        return False


    def search_matrix_v0(self, matrix: List[List[int]], target: int) -> bool:
        """
        Pruning
        T: (M + N)
        S: O(1)
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows - 1, 0

        while row >= 0 and col < cols:
            if target < matrix[row][col]:
                row -= 1
            elif target > matrix[row][col]:
                col += 1
            else:
                return True
        return False


if __name__ == "__main__":
    matrix = TwoDimensionalMatrix()
    print(matrix.search_matrix_v0(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    ))
    print(matrix.search_matrix_v0(
        [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13
    ))
    print(matrix.search_matrix_v0(
        [[1]], 1
    ))
    print(matrix.search_matrix_v0(
        [[1]], 9
    ))
    print(matrix.search_matrix_v0(
        [[]], 9
    ))
    print("___**___")
    print(matrix.search_matrix_v1(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    ))
    print(matrix.search_matrix_v1(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
    ))
    print(matrix.search_matrix_v1(
        [[1]], 1
    ))
    print(matrix.search_matrix_v1(
        [[1]], 9
    ))
    print(matrix.search_matrix_v1(
        [[]], 9
    ))