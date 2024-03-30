from typing import List


class SlidingWindow:

    def findSubStringWithConcatenationOfAllWords(self, s: str, words: List[str]) -> List[int]:
        """
        Approach: Two Pointers
        T: O((N - M) * M) GPT LC: O(a + n * b)
        S: O(N) LC: O(a + b)
        :param s:
        :param words:
        :return:
        """

        wordLen = len(words[0])
        totalWords = len(words)
        strLength = len(s)

        subStringLength = totalWords * wordLen

        if strLength < subStringLength:
            return []

        wordToFreq = {}

        for word in words:
            wordToFreq[word] = wordToFreq.get(word, 0) + 1

        result = []
        left = 0

        while left <= strLength - subStringLength:
            formed = 0
            subStringSeen = {}
            right = left
            while right < strLength:
                # if it is out of boundary
                if right + wordLen > strLength:
                    break

                subString = s[right: right + wordLen]
                subStringSeen[subString] = subStringSeen.get(subString, 0) + 1

                # if subString is not in current word or its freq is excess
                if subString not in wordToFreq or subStringSeen[subString] > wordToFreq[subString]:
                    break

                # increment the formed with word length
                formed += wordLen

                # if we found the substring add the start index of substring
                if formed == subStringLength:
                    result.append(left)
                # increment the right to next valid wordLen
                right += wordLen
            left += 1
        return result


if __name__ == "__main__":
    slidingWindow = SlidingWindow()
    print(slidingWindow.findSubStringWithConcatenationOfAllWords("barfoothefoobarman", ["foo", "bar"]))
    print(slidingWindow.findSubStringWithConcatenationOfAllWords("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(slidingWindow.findSubStringWithConcatenationOfAllWords("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
