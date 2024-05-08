

class HaystackNeedle:


    def str_str(self, haystack: str, needle: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param haystack:
        :param needle:
        :return:
        """

        n = len(needle)
        h = len(haystack)
        left = 0
        right = 0

        while left <= h - n:

            while right < n:

                if haystack[left + right] != needle[right]:
                    right = 0
                    break

                if right == n - 1:
                    return left
                right += 1
            left += 1
        return -1