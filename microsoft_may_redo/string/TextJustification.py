from typing import List


class TextJustification:

    def justify(self, words: List[str], max_width: int) -> List[str]:
        """
        Approach:
        T: O(n * k)
        S: O(m)
        :param words:
        :param max_width:
        :return:
        """

        def get_words_per_line(ptr: int):
            current_line = []
            curr_len = 0

            while ptr < len(words) and curr_len + len(words[ptr]) <= max_width:
                current_line.append(words[ptr])
                curr_len += len(words[ptr]) + 1
                ptr += 1
            return current_line

        def create_line(line: List[str], ptr: int):

            base_len = -1
            for word in line:
                base_len += len(word) + 1

            extra_spaces = max_width - base_len

            # edge case
            if len(line) == 1 or ptr == len(words):
                return ' '.join(line) + ' ' * extra_spaces

            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            extra_spaces_per_word = extra_spaces % word_count

            for i in range(extra_spaces_per_word):
                line[i] += ' '

            for i in range(word_count):
                line[i] += ' ' * spaces_per_word
            return ' '.join(line)

        ptr = 0
        output = []
        while ptr < len(words):
            curr_line = get_words_per_line(ptr)
            ptr += len(curr_line)
            output.append(create_line(curr_line, ptr))
        return output
