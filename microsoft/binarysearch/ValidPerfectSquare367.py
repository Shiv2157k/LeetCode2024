class ValidPerfectSquare:

    def isPerfectSquare(self, num: int) -> bool:
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
            elif pivot * pivot > num:
                right = pivot - 1
            else:
                left = pivot + 1
        return False
