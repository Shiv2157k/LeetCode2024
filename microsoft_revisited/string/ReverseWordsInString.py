from typing import List
from collections import deque



class ReverseWords:

    def reverseWordsV1(self, s: str) -> str:
        """
        Approach: Deque
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        left, right = 0, len(s) - 1

        while left <= right and s[left].isspace():
            left += 1

        while left <= right and s[right].isspace():
            right -= 1

        line = deque()
        word = []

        while left <= right:
            if s[left] == ' ' and word:
                line.appendleft(''.join(word))
                word = []
            elif not s[left].isspace():
                word.append(s[left])
            left += 1
        line.appendleft(''.join(word))
        return ''.join(line)


    def reverseWordsV0(self, s: str) -> str:
        """
        Approach: Trim, reverse and reverse each word
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        # step1: trim spaces
        line = self._trimSpaces(s)

        # step2: reverse line
        self._reverse(line, 0, len(line) - 1)

        # step3: reverse each word
        self._reverseEachWord(line)

        return ''.join(line)

    def _trimSpaces(self, s: str) -> List[chr]:

        left, right = 0, len(s) - 1

        while left < right and s[left].isspace():
            left += 1

        while left < right and s[right].isspace():
            right -= 1

        output = []

        while left < right:
            if not s[left].isspace():
                output.append(s[left])
            elif not output[-1].isspace():
                output.append(s[left])
            left += 1
        return output

    def _reverse(self, line: List[chr], left: int, right: int):
        while left < right:
            line[left], line[right] = line[right], line[left]
            left += 1
            right -= 1

    def _reverseEachWord(self, line: List[chr]) -> None:

        left, right = 0, 0

        while left < len(line):

            while right < len(line) and not line[right].isspace():
                right += 1
            self._reverse(line, left, right - 1)

            left = right + 1
            right += 1