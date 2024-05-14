class LongestSubstringWithoutRepeatingCharacters:

    def length_of_longest_substring_v1(self, s: str) -> int:
        """
        Approach: Last Occurrence
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        max_len = 0
        left = 0
        right = 0

        last_occurrence = {}

        while right < len(s):

            if s[right] in last_occurrence:
                left = max(left, last_occurrence[s[right]])
                
            last_occurrence[s[right]] = right + 1
            right += 1
            max_len = max(max_len, right - left)
        return max_len

    def length_of_longest_substring_v0(self, s: str) -> int:
        """
        Approach: Freq Char Map
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        max_len = 0
        left = 0
        right = 0
        char_freq = {}

        while right < len(s):

            char_freq[s[right]] = char_freq.get(s[right], 0) + 1

            while char_freq[s[right]] > 1:
                char_freq[s[left]] -= 1
                left += 1

            right += 1
            max_len = max(max_len, right - left)
        return max_len
