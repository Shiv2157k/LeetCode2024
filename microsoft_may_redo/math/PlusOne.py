from typing import List


class PlusOne:

    def plus_one(self, digits: List[int]) -> List[int]:
        """
        Approach: Math
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
