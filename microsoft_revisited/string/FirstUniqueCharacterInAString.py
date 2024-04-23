from typing import Dict


class String:

    def first_unique_char_index(self, s: str) -> int:
        """
        Approach: Hash Map
        T: O(N)
        S: O(1) -> as 26 is a constant
        :param s:
        :return: 
        """

        char_freq: Dict[str, int] = {}

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for ptr, char in enumerate(s):
            if char_freq[char] == 1:
                return ptr
        return -1
