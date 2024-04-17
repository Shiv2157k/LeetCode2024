class LongestSubstringWithAtMostKDistinct:

    def lengthOfLongestSubstringKDistinctV1(self, s: str, k: int) -> int:
        """
        Approach: Sliding Window II with maxSize as second pointer
        T: O(N)
        S: O(K)
        :param s:
        :param k:
        :return:
        """

        maxSize = 0
        right = 0
        counterMap = {}

        while right < len(s):

            counterMap[s[right]] = counterMap.get(s[right], 0) + 1

            if len(counterMap) <= k:
                maxSize += 1
            else:
                counterMap[s[right - maxSize]] -= 1
                if counterMap[s[right - maxSize]] == 0:
                    del counterMap[s[right - maxSize]]
            right += 1
        return maxSize

    def lengthOfLongestSubstringKDistinctV0(self, s: str, k: int) -> int:
        """
        Approach: Sliding Window with two pointers
        T: O(N)
        S: O(K)
        :param s:
        :param k:
        :return:
        """

        counterMap = {}
        left, right = 0, 0
        maxSize = 0

        while right < len(s):
            counterMap[s[right]] = counterMap.get(s[right], 0) + 1

            while len(counterMap) > k:
                counterMap[s[left]] -= 1
                if counterMap[s[left]] == 0:
                    del counterMap[s[left]]
                left += 1

            maxSize = max(maxSize, right - left + 1)
            right += 1
        return maxSize
