class NeedleInHayStack:

    def str_str(self, haystack: str, needle: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param haystack:
        :param needle:
        :return:
        """

        h = len(haystack)
        n = len(needle)

        left = 0

        while left <= h - n:
            right = 0
            while right < n:
                if haystack[left + right] != needle[right]:
                    break
                if right == n - 1:
                    return left
                right += 1
            left += 1
        return -1
