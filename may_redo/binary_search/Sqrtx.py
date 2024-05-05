class SquareRootX:

    def square_root_of_x(self, x: int) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param x:
        :return:
        """

        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            sqrt = pivot * pivot

            if sqrt == x:
                return pivot
            elif sqrt > x:
                right = pivot - 1
            elif sqrt < x:
                left = pivot + 1
        return right
