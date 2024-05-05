from typing import List


class StringCompression:

    def compression_length(self, chars: List[str]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param chars:
        :return:
        """

        writer: int = 0
        anchor: int = 0

        for reader in range(len(chars)):
            # case 1: if we reached the end of the array
            # case 2: if the adjacent character is not same
            if reader == len(chars) - 1 or chars[reader] == chars[reader + 1]:
                # make sure to add the anchor's char to writer
                chars[writer] = chars[anchor]
                writer += 1
                # if reader is farther than anchor
                # that means we have to compress
                if reader > anchor:
                    compress_len = str(reader - anchor + 1)
                    # add digits into the writer pointer
                    for digit in compress_len:
                        chars[writer] = digit
                        writer += 1
                anchor = reader + 1
        return writer
