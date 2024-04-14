from typing import List


class PascalTriangleII:

    def getRow(self, rowIndex: int) -> List[int]:
        """
        Approach: DP
        T: O(N^2)
        S: O(1)
        :param rowIndex:
        :return:
        """

        pascal = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):

            for j in range(1, i):
                pascal[i - j] = pascal[i - j] + pascal[i - j - 1]
        return pascal


if __name__ == "__main__":
    pascalTriangle = PascalTriangleII()
    print(pascalTriangle.getRow(4))
