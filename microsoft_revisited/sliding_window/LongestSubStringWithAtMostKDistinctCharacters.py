from typing import Dict


class SubString:

    def length_of_longest_k_distinct_v1(self, s: str, k: int) -> int:
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param s:
        :param k:
        :return:
        """
        max_len: int = 0
        char_freq: Dict[str, int] = {}
        right = 0

        while right < len(s):

            char_freq[s[right]] = char_freq.get(s[right], 0) + 1

            if len(char_freq) <= k:
                max_len += 1
            else:
                char_freq[s[right - max_len]] -= 1
                if char_freq[s[right - max_len]] == 0:
                    del char_freq[s[right - max_len]]
            right += 1
        return max_len

    def length_of_longest_k_distinct_v0(self, s: str, k: int) -> int:
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param s:
        :param k:
        :return:
        """
        char_freq: Dict[str, int] = {}
        max_len: int = 0
        left: int = 0
        right: int = 0

        while right < len(s):

            char_freq[s[right]] = char_freq.get(s[right], 0) + 1

            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
