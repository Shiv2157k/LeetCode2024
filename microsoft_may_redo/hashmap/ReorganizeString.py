class String:

    def reorganize(self, s: str) -> str:
        """
        Approach: FreqMap
        T: O(N)
        S: O(K)
        :param s:
        :return:
        """

        max_freq = 0
        max_freq_char = None
        char_freq = {}
        length = len(s)

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
            if char_freq[char] > max_freq:
                max_freq = char_freq[char]
                max_freq_char = char

        # validation
        if max_freq > (length + 1) // 2:
            return ''

        result = [''] * length
        ptr = 0

        while char_freq[max_freq_char] != 0:
            result[ptr] = max_freq_char
            ptr += 2
            char_freq[max_freq_char] -= 1

        for char in s:
            while char_freq[char] > 0:
                if ptr >= length:
                    ptr = 1
                result[ptr] = char
                ptr += 2
                char_freq[char] -= 1
        return ''.join(result)
