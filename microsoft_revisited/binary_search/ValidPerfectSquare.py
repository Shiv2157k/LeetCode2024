class PerfectSquare:

    def is_valid(self, num: int) -> bool:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param num:
        :return:
        """

        if num < 2:
            return True

        left: int = 2
        right: int = num // 2

        while left <= right:
            pivot: int = left + (right - left) // 2
            target: int = pivot * pivot

            if target == num:
                return True
            elif target < num:
                left = pivot + 1
            elif target > num:
                right = pivot - 1
        return False
