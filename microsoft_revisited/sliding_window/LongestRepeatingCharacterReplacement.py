from typing import Dict


class RepeatingCharacters:

    def longest_with_k_replacements(self, s: str, k: int) -> int:
        """
        Approach: Sliding Window
        T: O(M)
        S: O(M)
        :param s:
        :param k:
        :return:
        """

        # two pointers to slide
        left: int = 0
        right: int = 0
        max_len: int = 0
        max_freq: int = 0
        char_freq: Dict[str, int] = {}

        while right < len(s):

            char_freq[s[right]] = char_freq.get(s[right], 0) + 1
            max_freq = max(max_freq, char_freq[s[right]])
            right += 1

            is_valid: bool = (right - left - max_freq <= k)
            if not is_valid:
                char_freq[s[left]] -= 1
                left += 1
            max_len = right - left
        return max_len
