from typing import List


class SpiralMatrix:

    def get_spiral(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Setting Boundaries
        T: O(M*N)
        S: O(1) -> not considering output
        :param matrix:
        :return:
        """

        row_boundary, col_boundary = len(matrix), len(matrix[0])
        curr_col, curr_row = -1, 0
        direction = 1
        spiral_output = []

        while (row_boundary * col_boundary) > 0:
            # move horizontally right and left
            for _ in range(col_boundary):
                # adjusting directions for right/ left
                curr_col += direction
                spiral_output.append(matrix[curr_row][curr_col])
            # adjust the row boundary decrementing by 1
            # as we don't visit that boundary anymore
            row_boundary -= 1
            # move vertically down and up
            for _ in range(row_boundary):
                # adjusting direction for down / up
                curr_row += direction
                spiral_output.append(matrix[curr_row][curr_col])
            # adjust the col boundary decrementing by 1
            # as we don't visit that boundary anymore
            col_boundary -= 1
            # flip direction to move up, right, left and down
            direction *= -1
        return spiral_output


if __name__ == "__main__":
    spiral_matrix = SpiralMatrix()
    print(spiral_matrix.get_spiral(
        [
            [2, 3, 4], [5, 6, 7], [8, 9, 10], [17, 18, 19]
        ]
    ))
    print(spiral_matrix.get_spiral(
        [
            [2, 3, 4], [5, 6, 7], [8, 9, 10]
        ]
    ))
    print(spiral_matrix.get_spiral(
        [
            [2, 3, 4], [5, 6, 7]
        ]
    ))
    print(spiral_matrix.get_spiral(
        [
            [2, 3, 4]
        ]
    ))
    print(spiral_matrix.get_spiral(
        [
            [2, 3]
        ]
    ))
    print(spiral_matrix.get_spiral(
        [
            [2]
        ]
    ))