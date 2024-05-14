from typing import List


class StringCompression:


    def compress_and_get_length(self, chars: List[str]) -> int:
        """
        Approach: Three Pointers
        T: O(N)
        S: O(1)
        :param chars:
        :return:
        """
        # a, a, a, b, b, c, c -> a, b, c, 3, 2, 2
        writer = 0
        anchor = 0

        for reader in range(len(chars)):

            if reader == len(chars) - 1 or chars[reader] != chars[reader + 1]:

                chars[writer] = chars[anchor]
                writer += 1

                if reader > anchor:
                    compress_len = str(reader - anchor + 1)
                    for digit in compress_len:
                        chars[writer] = digit
                        writer += 1
                anchor = reader + 1
        return writer