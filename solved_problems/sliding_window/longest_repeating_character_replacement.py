

class CharacterReplacement:

    def LongestRepeatingV2(self, s: str, k: int) -> int:
        """
        Approach: Sliding Window Fast
        T: O(N)
        S: O(N)
        :param s:
        :param k:
        :return:
        """
        freqMap = {}
        left = right = 0
        maxFreq = maxLen = 0

        while right < len(s):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[right]])
            right += 1

            isValidWindow = (right - left - maxFreq <= k)

            if not isValidWindow:
                freqMap[s[left]] -= 1
                left += 1

            maxLen = right - left
        return maxLen

    def LongestRepeatingV1(self, s: str, k: int) -> int:
        """
        Approach: Sliding Window slow
        T: O(MN)
        S: O(N)
        :param s:
        :param k:
        :return:
        """
        char_set = set(s)
        maxLen = 0

        for char in char_set:
            count = left = right = 0
            while right < len(s):

                if s[right] == char:
                    count += 1
                right += 1

                while not right - left - count <= k:
                    if s[left] == char:
                        count -= 1
                    left += 1
                maxLen = max(maxLen, right - left)
        return maxLen


    def LongestRepeatingV0(self, s: str, k: int) -> int:
        """
        Approach: Binary Search + Sliding Window
        T: O(N log N)
        S: O(1)
        :param s:
        :param k:
        :return:
        """

        left, right = 1, len(s) + 1

        # Binary Search
        while left + 1 < right:
            pivot = left + (right - left) // 2
            if self.__canMakeSubstring(pivot, s, k):
                left = pivot
            else:
                right = pivot
        return left

    def __canMakeSubstring(self, subStringLength, s: str, k: int) -> bool:
        """
        Fixed Sliding Window
        :param subStringLength:
        :param s:
        :param k:
        :return:
        """
        left = right = 0
        freqMap = {}
        maxFreq = 0

        while right < len(s):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1

            if right + 1 - left > subStringLength:
                freqMap[s[left]] -= 1
                left += 1

            maxFreq = max(maxFreq, freqMap[s[right]])
            right += 1

            if subStringLength - maxFreq <= k:
                return True
        return False


if __name__ == "__main__":
    characterReplacement = CharacterReplacement()
    print(characterReplacement.LongestRepeatingV0("AABABBA", 1))
    print(characterReplacement.LongestRepeatingV0("AABABBA", 2))
    print("<(**_|_**)>")
    print(characterReplacement.LongestRepeatingV1("AABABBA", 1))
    print(characterReplacement.LongestRepeatingV1("AABABBA", 2))
    print("<(**_|_**)>")
    print(characterReplacement.LongestRepeatingV2("AABABBA", 1))
    print(characterReplacement.LongestRepeatingV2("AABABBA", 2))