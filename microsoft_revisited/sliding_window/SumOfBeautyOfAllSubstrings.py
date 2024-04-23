class BeautyOfAllSubstrings:

    def beautySum(self, s: str) -> int:
        """
        Approach: Sliding Window/ Two Pointers
        T: O(N^2)
        S: O(N)
        :param s:
        :return:
        """

        result = 0
        left = 0

        while left < len(s):
            freqMap = {}
            freqMap[s[left]] = freqMap.get(s[left], 0) + 1
            maxFreq, minFreq = 1, 1

            right = left + 1

            while right < len(s):
                freqMap[s[right]] = freqMap.get(s[right], 0) + 1
                maxFreq = max(maxFreq, freqMap[s[right]])
                minFreq = min(freqMap.values())
                result += maxFreq - minFreq
                right += 1
            left += 1
        return result
