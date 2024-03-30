class HayStack:

    def findNeedle(self, haystack: str, needle: str) -> int:
        """
        Approach: Sliding Window
        T: O(NM)
        S: O(1)
        :param haystack:
        :param needle:
        :return:
        """

        h = len(haystack)
        n = len(needle)

        left = right = 0

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


if __name__ == "__main__":
    haystackInNeedle = HayStack()
    print(haystackInNeedle.findNeedle("sadbutsad", "sad"))
    print(haystackInNeedle.findNeedle("leetcode", "leeto"))
    print(haystackInNeedle.findNeedle("leetcode", "code"))
