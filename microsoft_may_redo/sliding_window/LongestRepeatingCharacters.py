class LongestRepeatingCharacterReplacement:

    def character_replacement(self, s: str, k: int) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param s:
        :param k:
        :return:
        """

        left = 0
        right = 0
        max_freq = 0
        max_len = 0

        char_freq = {}

        while right < len(s):

            char_freq[s[right]] = char_freq.get(s[right], 0) + 1
            max_freq = max(max_freq, char_freq[s[right]])

            right += 1
            
            is_valid = (right - left - max_freq <= k)
            if not is_valid:
                char_freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len

