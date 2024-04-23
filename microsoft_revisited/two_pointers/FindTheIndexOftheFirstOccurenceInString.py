

class String:


    def findFirstOccurrence(self, haystack: str, needle: str) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param haystack:
        :param needle:
        :return:
        """

        h = len(haystack)
        n = len(needle)

        left, right = 0, 0

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