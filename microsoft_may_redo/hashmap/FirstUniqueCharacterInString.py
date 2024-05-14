class FirstUniqueCharacter:

    def first_unique_char_pos(self, s: str) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        char_freq = {}

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for ptr, char in s:
            if char_freq[char] == 1:
                return ptr
        return -1
