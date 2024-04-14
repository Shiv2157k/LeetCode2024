from typing import List


class GrayCode:

    def generate(self, n: int) -> List[int]:
        """
        Approach: Bit Manipulation
        T: O(2^n)
        S: O(1)
        :param n:
        :return:
        """
        result = []

        for num in range(1 << n):
            result.append(num ^ (num >> 1))
        return result


if __name__ == "__main__":
    grayCode = GrayCode()
    print(grayCode.generate(2))
    print(grayCode.generate(3))
    print(grayCode.generate(1))
