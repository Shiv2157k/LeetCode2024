from typing import List


class PlusOne:

    def plusOneV1(self, digits: List[int]) -> List[int]:
        """
        Approach: As per rules with for loop
        T: O(N)
        S: O(1)
        :param digits:
        :return:
        """
        n = len(digits)
        
        for i in range(n):
            pointer = n - i - 1

            if digits[pointer] == 9:
                digits[pointer] = 0
            else:
                digits[pointer] += 1
                return digits
        return [1] + digits

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Approach: As per rules
        T: O(N)
        S: O(1)
        :param digits:
        :return:
        """

        # case 1: 123
        # case 2: 129 -> digits[0] = 0 digits[1] += 1
        # case 3: 99 -> digits[0] = 1 all remaining 0

        pointer = len(digits) - 1

        while pointer >= 0:

            if digits[pointer] == 9:
                digits[pointer] = 0
            else:
                digits[pointer] += 1
                return digits
            pointer -= 1
        return [1] + digits
