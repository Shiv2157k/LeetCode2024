


class Word:

    def get_length_of_last_word_v1(self, s: str) -> int:
        """
        Approach: one pass
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        ptr = len(s) - 1
        length = 0

        while ptr >= 0:
            if not s[ptr].isspace():
                length += 1
            elif length > 0:
                return length
            ptr -= 1
        return length

    def get_length_of_last_word_v0(self, s: str) -> int:
        """
        Approach: Two Pass
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        ptr = len(s) - 1

        while ptr >= 0 and s[ptr].isspace():
            ptr -= 1

        length = 0

        while ptr >= 0 and not s[ptr].isspace():
            ptr -= 1
            length += 1
        return length



