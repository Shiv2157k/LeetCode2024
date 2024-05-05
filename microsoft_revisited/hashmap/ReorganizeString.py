from typing import Dict


class String:

    def reorganize(self, s: str) -> str:
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        length = len(s)
        char_freq_map: Dict[str, int] = {}
        max_freq = 0
        max_freq_char = None

        for char in s:
            char_freq_map[char] = char_freq_map.get(char, 0) + 1
            if max_freq < char_freq_map[char]:
                max_freq = char_freq_map[char]
                max_freq_char = char

        # validation
        if max_freq > (length + 1) // 2:
            return ''

        result = [''] * length
        ptr = 0

        while char_freq_map[max_freq_char] != 0 and ptr < length:
            result[ptr] = max_freq_char
            ptr += 2
            char_freq_map[max_freq_char] -= 1

        for char in s:
            while char_freq_map[char] > 0:
                if ptr >= length:
                    ptr = 1
                result[ptr] = char
                ptr += 2
                char_freq_map[char] -= 1
        return ''.join(result)
