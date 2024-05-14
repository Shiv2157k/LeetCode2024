class PalindromeNumber:

    def is_palindrome_number(self, x: int) -> bool:
        """
        Approach: BS
        T: O(log N)
        S: O(1)
        :param x:
        :return:
        """

        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0

        while x > half:
            half = half * 10 + x % 10
            x //= 10
        return x == half or x == half // 10
