from typing import List


class ReverseWordsInString:

    def reverse_words(self, s: str) -> str:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        # 1: trim spaces
        line = self.__trim_spaces(s)
        # 2: reverse line
        self.__reverse(line, 0, len(line) - 1)
        # 3: reverse each word
        self.__reverse_each_word(line)
        return ''.join(line)

    def __trim_spaces(self, s: str) -> List[str]:

        left = 0
        right = len(s) - 1

        while left < right and s[left].isspace():
            left += 1
        while left < right and s[right].isspace():
            right -= 1

        output = []

        while left <= right:
            if not s[left].isspace():
                output.append(s[left])
            elif not output[-1].isspace():
                output.append(s[left])
            left += 1
        return output

    def __reverse(self, line: List[str], left: int, right: int) -> None:
        while left <= right:
            line[left], line[right] = line[right], line[left]
            left += 1
            right -= 1

    def __reverse_each_word(self, line: List[str]) -> None:
        left = 0
        right = 0

        while left < len(line):

            while right < len(line) and not line[right].isspace():
                right += 1
            self.__reverse(line, left, right - 1)
            left = right + 1
            right += 1
