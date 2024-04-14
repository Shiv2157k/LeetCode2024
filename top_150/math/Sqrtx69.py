class Sqrt:

    def ofNumber(self, x: int) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param x:
        :return:
        """

        left, right = 0, x // 2

        while left <= right:

            pivot = left + (right - left) // 2
            target = pivot * pivot

            if target < x:
                left = pivot + 1
            elif target > x:
                right = pivot - 1
            else:
                return pivot
        return right


if __name__ == "__main__":
    sqrt = Sqrt()
    print(sqrt.ofNumber(9))
    print(sqrt.ofNumber(8))
    print(sqrt.ofNumber(17))
