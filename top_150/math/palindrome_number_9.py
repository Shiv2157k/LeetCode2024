


class PalindromeNumber:

    def is_palindrome(self, x: int) -> bool:
        """
        Approach: Half Comparison
        T :O( log base 10 (n))
        S: O(1)
        :param x:
        :return:
        """
        # base case
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0
        while x > half:
            half = half * 10 + x % 10
            x = x // 10
        return x == half or x == half // 10


if __name__ == "__main__":

    palindromeNum = PalindromeNumber()
    print(palindromeNum.is_palindrome(121))
    print(palindromeNum.is_palindrome(1221))
    print(palindromeNum.is_palindrome(1))
    print(palindromeNum.is_palindrome(-121))
    print(palindromeNum.is_palindrome(+121))
    print(palindromeNum.is_palindrome(120))
