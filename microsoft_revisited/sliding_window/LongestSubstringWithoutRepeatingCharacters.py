class LongestSubstring:

    def withoutRepeatingCharactersV1(self, s: str) -> int:
        """
        Approach: Sliding Window Optimized
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        if not s:
            return 0
        if len(s) <= 1:
            return len(s)

        lastOccurrence = {}

        left, right, maxLen = 0, 0, 0

        while right < len(s):

            if s[right] in lastOccurrence:
                left = max(left, lastOccurrence[s[right]])

            lastOccurrence[s[right]] = right + 1
            right += 1

            maxLen = max(maxLen, right - left)
        return maxLen

    def withoutRepeatingCharactersV0(self, s: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        # validation
        if not s:
            return 0
        if len(s) <= 1:
            return len(s)

        freqChar = {}

        left, right = 0, 0
        maxLen = 0

        while right < len(s):

            freqChar[s[right]] = freqChar.get(s[right], 0) + 1

            while freqChar[s[right]] > 1:
                freqChar[s[left]] -= 1
                left += 1
            right += 1
            maxLen = max(maxLen, right - left)

        return maxLen
