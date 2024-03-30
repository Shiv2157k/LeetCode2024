class String:

    def lengthOfLongestSubstringWithoutRepeatingCharactersV1(self, s: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        lastOccurrence = {}
        maxLen = left = right = 0

        while right < len(s):

            if s[right] in lastOccurrence:
                left = max(left, lastOccurrence[s[right]])

            lastOccurrence[s[right]] = right + 1
            right += 1

            maxLen = max(maxLen, right - left)
        return maxLen

    def lengthOfLongestSubstringWithoutRepeatingCharactersV0(self, s: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        charFreq = {}
        maxLen = left = right = 0

        while right < len(s):

            rightChar = s[right]
            charFreq[rightChar] = charFreq.get(rightChar, 0) + 1

            while charFreq[rightChar] > 1:
                leftChar = s[left]
                charFreq[leftChar] -= 1
                left += 1
            right += 1
            maxLen = max(maxLen, right - left)
        return maxLen


if __name__ == "__main__":

    string = String()
    print(string.lengthOfLongestSubstringWithoutRepeatingCharactersV0("abcabcbb"))
    print(string.lengthOfLongestSubstringWithoutRepeatingCharactersV0("bbbbb"))
    print(string.lengthOfLongestSubstringWithoutRepeatingCharactersV0("pwwkew"))

    print(string.lengthOfLongestSubstringWithoutRepeatingCharactersV1("abcabcbb"))
    print(string.lengthOfLongestSubstringWithoutRepeatingCharactersV1("bbbbb"))
    print(string.lengthOfLongestSubstringWithoutRepeatingCharactersV1("pwwkew"))
