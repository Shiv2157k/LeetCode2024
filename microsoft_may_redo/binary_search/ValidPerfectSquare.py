class ValidPerfectSquare:

    def is_valid_perfect_square(self, num: int) -> bool:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param num:
        :return:
        """

        if num < 2:
            return True

        left = 2
        right = num // 2

        while left <= right:
            pivot = left + (right - left) // 2

            if pivot * pivot == num:
                return True
            elif pivot * pivot < num:
                left = pivot + 1
            else:
                right = pivot - 1
        return False
