from typing import List


class PlusOne:

    def plus_one_v2(self, digits: List[int]) -> List[int]:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
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
            pointer -= 1
        return [1] + digits

    def plus_one_v1(self, digits: List[int]) -> List[int]:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param digits:
        :return:
        """
        n = len(digits)
        for i in range(n):

            if digits[n - 1 - i] == 9:
                digits[n - 1 - i] = 0
            else:
                digits[n - 1 - i] += 1
                return digits
        return [1] + digits
