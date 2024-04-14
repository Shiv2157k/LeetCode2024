from typing import List


class TextJustification:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def getWordsPerLine(ptr: int) -> List[str]:
            currentLine = []
            currLen = 0

            while ptr < len(words) and currLen + len(words[ptr]) <= maxWidth:
                currentLine.append(words[ptr])
                currLen += len(words[ptr]) + 1
                ptr += 1
            return currentLine

        def createLine(line: List[str], ptr: int) -> str:

            baseLen = -1

            for word in line:
                baseLen += len(word) + 1

            extraSpaces = maxWidth - baseLen

            # edge case
            if len(line) == 1 or ptr == len(words):
                return " ".join(line) + " " * extraSpaces

            wordCount = len(line) - 1
            spacesPerWord = extraSpaces // wordCount
            extraSpacesPerWord = extraSpaces % wordCount

            for i in range(extraSpacesPerWord):
                line[i] += " "

            for i in range(wordCount):
                line[i] += " " * spacesPerWord
            return " ".join(line)

        ans = []
        index = 0

        while index < len(words):
            currLine = getWordsPerLine(index)
            index += len(currLine)
            ans.append(createLine(currLine, index))
        return ans
