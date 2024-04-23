from typing import List


class TextJustification:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Approach: As per rules provided
        T: O(N * K)
        S: O(M)
        :param words:
        :param maxWidth:
        :return:
        """
        ptr = 0
        output = []
        while ptr < len(words):
            currentLine = self._getWordsPerLine(ptr, words, maxWidth)
            ptr += len(currentLine)
            output.append(self._createLine(currentLine, ptr, maxWidth, len(words)))
        return output

    def _getWordsPerLine(self, ptr: int, words: List[str], maxWidth: int) -> List[str]:
        currentLine = []
        currentLen = 0

        while ptr < len(words) and currentLen + len(words[ptr]) <= maxWidth:
            currentLine.append(words[ptr])
            currentLen += len(words[ptr]) + 1
            ptr += 1
        return currentLine

    def _createLine(self, line: List[str], ptr: int, maxWidth: int, wordLen: int) -> str:

        baseLen = -1
        for word in line:
            baseLen += len(word) + 1

        extraSpaces = maxWidth - baseLen
        # edgeCases
        if len(line) == 1 or ptr == wordLen:
            return ' '.join(line) + " " * extraSpaces

        wordCount = len(line) - 1
        spacesPerWord = extraSpaces // wordCount
        extraSpacesPerWord = extraSpaces % wordCount

        for i in range(extraSpacesPerWord):
            line[i] += " "

        for i in range(wordCount):
            line[i] += " " * spacesPerWord

        return ' '.join(line)
