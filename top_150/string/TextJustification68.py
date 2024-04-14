from typing import List


class TestJustification:


    def justify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Approach:
        T: O(n * k)
        S: O(m)
        :param words:
        :param maxWidth:
        :return:
        """

        def getWordsPerLine(ptr: int) -> List[str]:
            currLine = []
            currentLen = 0

            while ptr < len(words) and currentLen + len(words[ptr]) <= maxWidth:
                currLine.append(words[ptr])
                currentLen += len(words[ptr]) + 1
                ptr += 1
            return currLine

        def createLine(line: List[str], ptr: int):

            baseLen = -1
            for word in line:
                # + 1 for considering mandatory
                baseLen += len(word) + 1

            # edge case: last line or a line with single word
            extraSpaces = maxWidth - baseLen
            if len(line) == 1 or ptr == len(words):
                return " ".join(line) + " " * extraSpaces

            # regular line
            wordCount = len(line) - 1
            spacesPerWord = extraSpaces // wordCount
            extraSpacesNeeded = extraSpaces % wordCount

            # add extraSpaces prioritizing from left
            for j in range(extraSpacesNeeded):
                line[j] += " "
            for j in range(wordCount):
                line[j] += " " * spacesPerWord
            return " ".join(line)

        ans = []
        index = 0

        while index < len(words):
            currentLine = getWordsPerLine(index)
            index += len(currentLine)
            ans.append(createLine(currentLine, index))
        return ans


if __name__ == "__main__":
    textJustification = TestJustification()
    print(textJustification.justify(["This", "is", "an", "example", "of", "text", "justification."], 16))