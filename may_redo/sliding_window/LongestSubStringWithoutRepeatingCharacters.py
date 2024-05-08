class LongestSubStringWithoutRepeatingCharacters:

    def longest_substr_without_repeating_chars_v1(self, s: str) -> int:
        """
        Approach: SlidingWindow
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        left = 0
        right = 0
        max_len = 1
        last_occurrences = {}

        while right < len(s):

            if s[right] in last_occurrences:
                left = max(last_occurrences[s[right]], left)

            last_occurrences[s[right]] = right + 1
            right += 1
            max_len = max(max_len, right - left)
        return max_len

    def longest_substr_without_repeating_chars_v0(self, s: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        left = 0
        right = 0
        char_freq_map = {}
        max_len = 1

        while right < len(s):

            right_char = s[right]

            char_freq_map[right_char] = char_freq_map.get(right_char, 0) + 1

            if char_freq_map[right_char] > 1:
                left_char = s[left]
                char_freq_map[left_char] -= 1
                left += 1
            right += 1
            max_len = max(max_len, right - left)
        return max_len
