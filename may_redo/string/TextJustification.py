from typing import List


class TextJustification:

    def full_justify(self, words: List[str], max_width: int) -> List[str]:
        """
        Approach: AS per constraints
        T: O(N * K)
        S: O(M)
        :param words:
        :param max_width:
        :return:
        """

        ptr = 0
        lines = []
        while ptr < len(words):
            curr_line = self._get_words_per_line(ptr, words, max_width)
            ptr += len(curr_line)
            lines.append(self._create_line(curr_line, ptr, len(words), max_width))
        return lines

    def _get_words_per_line(self, ptr: int, words: List[str], max_width: int) -> List[str]:
        curr_line = []
        curr_len = 0
        while ptr < len(words) and curr_len + len(words[ptr]) <= max_width:
            curr_line.append(words[ptr])
            curr_len += len(words[ptr]) + 1
            ptr += 1

        return curr_line

    def _create_line(self, line: List[str], ptr: int, word_len: int, max_width: int) -> str:
        base_len = -1
        for word in line:
            base_len += len(word) + 1

        extra_spaces = max_width - base_len

        # edge case
        if len(line) == 1 or ptr == word_len:
            return ' '.join(line) + ' ' * extra_spaces

        word_count = len(line) - 1
        spaces_per_word = extra_spaces // word_count
        extra_spaces_per_word = extra_spaces % word_count

        for i in range(extra_spaces_per_word):
            line[i] += ' '

        for i in range(word_count):
            line[i] += ' ' * spaces_per_word
        return ' '.join(line)
