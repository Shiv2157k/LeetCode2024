class Palindrome:

    def isValid(self, s: str) -> bool:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        left, right = 0, len(s) - 1

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


if __name__ == "__main__":
    pal = Palindrome()
    print(pal.isValid("A man, a plan, a canal: Panama"))
    print(pal.isValid("race a car"))
    print(pal.isValid(" "))
