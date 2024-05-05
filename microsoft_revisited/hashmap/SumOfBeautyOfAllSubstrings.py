from math import inf
from typing import Dict


class Strings:

    def sum_of_beauty_of_all_substrings(self, s: str) -> int:
        """
        Approach: Two Pointers and HashMap
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        total_sum: int = 0
        left: int = 0

        while left < len(s):

            freq_map: Dict[str, int] = {}
            freq_map[s[left]] = freq_map.get(s[left], 0) + 1
            max_freq: int = 1
            min_freq = s[left]

            right: int = left + 1

            while right < len(s):
                freq_map[s[right]] = freq_map.get(s[right], 0) + 1
                max_freq = max(max_freq, freq_map[s[right]])
                min_freq = min(freq_map.values())
                total_sum += max_freq - min_freq
                right += 1
            left += 1
        return total_sum
