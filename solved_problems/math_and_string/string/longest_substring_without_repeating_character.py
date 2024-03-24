class RepeatingCharacterString:

    def lengthOfLongestDistinctSubstringV1(self, s: str) -> int:
        """
        Approach: Sliding Window Optimized
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        lastOccurrence = {}
        left = right = 0
        maxLen = 0

        while right < len(s):

            if s[right] in lastOccurrence:
                left = max(left, lastOccurrence[s[right]])

            lastOccurrence[s[right]] = right + 1
            right += 1
            maxLen = max(maxLen, right - left)
        return maxLen

    def lengthOfLongestDistinctSubstringV0(self, s: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        freqChar = {}
        left = right = 0
        maxLen = 0

        while right < len(s):
            rightChar = s[right]
            freqChar[rightChar] = freqChar.get(rightChar, 0) + 1

            while freqChar[rightChar] > 1:
                leftChar = s[left]
                freqChar[leftChar] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen


if __name__ == "__main__":
    string = RepeatingCharacterString()
    print(string.lengthOfLongestDistinctSubstringV0("abcabcbb"))
    print(string.lengthOfLongestDistinctSubstringV1("abcabcbb"))
    print("__**__")
    print(string.lengthOfLongestDistinctSubstringV0("aaaaa"))
    print(string.lengthOfLongestDistinctSubstringV1("aaaaa"))
    print("__**__")
    print(string.lengthOfLongestDistinctSubstringV0(""))
    print(string.lengthOfLongestDistinctSubstringV1(""))
    print("__**__")
    print(string.lengthOfLongestDistinctSubstringV0("abaad"))
    print(string.lengthOfLongestDistinctSubstringV1("abaad"))
    print("__**__")
