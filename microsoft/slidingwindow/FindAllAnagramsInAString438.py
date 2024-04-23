from typing import List


class Anagrams:

    def findAllStartIndicesV1(self, s: str, p: str) -> List[int]:
        """
        Approach: Sliding Window + Array
        T: O(Ns)
        S: O(N + S)
        :param s:
        :param p:
        :return:
        """

        if len(s) < len(p):
            return []

        ns = len(s)
        np = len(p)

        pFreqBucket = [0] * 26
        sFreqBucket = [0] * 26

        for char in p:
            pFreqBucket[ord(char) - ord('a')] += 1

        right = 0
        output = []
        while right < ns:

            sFreqBucket[ord(s[right]) - ord('a')] += 1

            if right >= np:
                sFreqBucket[ord(s[right - np]) - ord('a')] -= 1

            if sFreqBucket == pFreqBucket:
                output.append(right - np + 1)
            right += 1
        return output

    def findAllStartIndicesV0(self, s: str, p: str) -> List[int]:
        """
        Approach: Sliding Window + HashMap
        T: O(Ns)
        S: O(Ns)
        :param s:
        :param p:
        :return:
        """

        # validation
        if len(s) < len(p):
            return []

        ns = len(s)
        np = len(p)

        pFreqMap = {}
        for char in p:
            pFreqMap[char] = pFreqMap.get(char, 0) + 1

        right = 0
        sFreqMap = {}
        output = []

        while right < ns:

            sFreqMap[s[right]] = sFreqMap.get(s[right], 0) + 1

            if len(sFreqMap) >= np:
                if sFreqMap[s[right - np]] == 1:
                    del sFreqMap[s[right - np]]
                else:
                    sFreqMap[s[right - np]] -= 1

            if sFreqMap == pFreqMap:
                output.append(right - np + 1)
            right += 1
        return output
