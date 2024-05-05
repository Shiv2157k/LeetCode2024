class Palindrome:

    def is_valid(self, s: str) -> bool:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        left: int = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
