from heapq import heappush, heappop


class String:

    def re_organize_with_no_same_adjacent_chars_v1(self, strs: str) -> str:
        """
        Approach: Counting and Even/Odd Arrangement
        T: O(N)
        S: O(N)
        :param strs:
        :return:
        """
        char_freq = {}

        for char in strs:
            char_freq[char] = char_freq.get(char, 0) + 1

        letter = ''
        max_freq = 0

        # to get max count and the char
        for char, freq in char_freq.items():
            if freq > max_freq:
                max_freq = freq
                letter = char

        if max_freq > (len(strs) + 1) // 2:
            return ''

        index = 0
        result = [''] * len(strs)
        while max_freq != 0:
            result[index] = letter
            max_freq -= 1
            index += 2

        for char, freq in char_freq.items():
            while freq > 0:
                if index >= len(strs):
                    index = 1
                result[index] = char
                index += 2
                freq -= 1
        return ''.join(result)

    def re_organize_with_no_same_adjacent_chars(self, strs: str) -> str:
        """
        Approach: HashMap Counter and Max Heap
        T: O(N log k) -> max of 3 priority queue operations
        S: O(N)
        :param strs:
        :return:
        """

        char_freq = {}
        max_heap = []
        # to store char and freq
        for char in strs:
            char_freq[char] = char_freq.get(char, 0) + 1

        for char, freq in char_freq.items():
            heappush(max_heap, (-freq, char))

        prev_freq, prev_char = 0, ''
        reorganized = []

        while max_heap:
            freq, char = heappop(max_heap)
            reorganized.append(char)

            if prev_freq != 0:
                heappush(max_heap, (prev_freq, prev_char))
            freq += 1
            prev_freq, prev_char = freq, char

        if len(reorganized) != len(strs):
            return ''
        return ''.join(reorganized)


if __name__ == "__main__":
    string = String()
    print(string.re_organize_with_no_same_adjacent_chars("aab"))
    print(string.re_organize_with_no_same_adjacent_chars_v1("aab"))
    print(string.re_organize_with_no_same_adjacent_chars("aa"))
    print(string.re_organize_with_no_same_adjacent_chars_v1("aa"))
    print(string.re_organize_with_no_same_adjacent_chars("aabbaacdar"))
    print(string.re_organize_with_no_same_adjacent_chars_v1("aabbaacdar"))



