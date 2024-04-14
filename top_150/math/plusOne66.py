from typing import List


class PlusOne:

    def getResultV1(self, digits: List[int]) -> List[int]:
        """
        Approach: SchoolBook Addition with Carry
        T: O(N)
        S: O(N)
        :param digits:
        :return:
        """

        pointer = len(digits) - 1

        while pointer >= 0:
            if digits[pointer] == 9:
                digits[pointer] = 0
            else:
                digits[pointer] += 1
                return digits
        return [0] + digits

    def getResultV0(self, digits: List[int]) -> List[int]:
        """
        Approach: SchoolBook Addition with Carry
        T: O(N)
        S: O(N)
        :param digits:
        :return:
        """
        n = len(digits)

        for index in range(n):
            ptr = n - 1 - index

            if digits[ptr] == 9:
                digits[ptr] = 0
            else:
                digits[ptr] += 1
                return digits
        return [1] + digits


if __name__ == "__main__":
    plusOne = PlusOne()
    print(plusOne.getResultV0([1, 9]))
    print(plusOne.getResultV0([9, 9]))
    print(plusOne.getResultV0([1, 8]))
