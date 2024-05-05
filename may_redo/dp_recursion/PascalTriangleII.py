from typing import List


class PascalTriangleII:

    def get_row(self, row_index: int) -> List[int]:
        """
        Approach: DP
        T: O(N^2)
        S: O(1)
        :param row_index:
        :return:
        """
        pascal = [1] * (row_index + 1)

        for row in range(2, row_index + 1):
            for col in range(1, row):
                pascal[row - col] = pascal[row - col] + pascal[row - col - 1]
        return pascal
