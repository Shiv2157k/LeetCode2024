class MinimumSubstring:

    def inSubStringV1(self, s: str, t: str) -> str:
        """
        Approach: Sliding Window Optimized
        T: O(|S| + |T|)
        S: O(|S| + |T|)
        :param s:
        :param t:
        :return:
        """
        if not s or not t:
            return ""

        freqT = {}
        for char in t:
            freqT[char] = freqT.get(char, 0) + 1

        filteredS = []
        for index, char in enumerate(s):
            if char in freqT:
                filteredS.append((index, char))

        left = right = 0
        formed, required = 0, len(freqT)
        windowCharFreq = {}
        windowMetaData = (float("inf"), None, None)

        while right < len(filteredS):

            char = filteredS[right][1]

            windowCharFreq[char] = windowCharFreq.get(char, 0) + 1

            if char in freqT and windowCharFreq[char] == freqT[char]:
                formed += 1

            while left <= right and formed == required:
                char = filteredS[left][1]
                # note left -> right and start -> end are two different things here
                start, end = filteredS[left][0], filteredS[right][0]

                if end - start + 1 < windowMetaData[0]:
                    windowMetaData = (end - start + 1, start, end)

                windowCharFreq[char] -= 1

                if windowCharFreq[char] < freqT[char]:
                    formed -= 1
                left += 1

            right += 1
        return "" if windowMetaData[0] == float("inf") else s[windowMetaData[1]: windowMetaData[2] + 1]

    def inSubStringV0(self, s: str, t: str) -> str:
        """
        Approach: Sliding Window
        T: O(|S| + |T|)
        S: O(|S| + |T|) * |S|
        :param s:
        :param t:
        :return:
        """
        if not s or not t:
            return ""

        freqT = {}
        for char in t:
            freqT[char] = freqT.get(char, 0) + 1

        left = right = 0
        formed, required = 0, len(t)
        windowCharFreq = {}
        # metadata contains -> window length, left and right pointer information
        windowMetaData = (float("inf"), None, None)

        while right < len(s):
            char = s[right]

            # add this char freq into the window char freq
            windowCharFreq[char] = windowCharFreq.get(char, 0) + 1

            # check if a letter is formed or not
            # if formed increment formed
            if char in freqT and windowCharFreq[char] == freqT[char]:
                formed += 1

            # Time to check if the current window can be contracted to
            # make desired minimum window
            while left <= right and formed == required:
                char = s[left]

                # check and capture if there is a min window so far
                if right - left + 1 < windowMetaData[0]:
                    windowMetaData = (right - left + 1, left, right)
                # decrement as this is no longer considered in our current window
                windowCharFreq[char] -= 1

                if char in freqT and windowCharFreq[char] < freqT[char]:
                    formed -= 1
                # to check for a new min desirable window increment left
                left += 1
            # keep expanding once we are done with contracting
            right += 1
        return "" if windowMetaData[0] == float("inf") else s[windowMetaData[1]: windowMetaData[2] + 1]


if __name__ == "__main__":
    minSubstring = MinimumSubstring()
    print(minSubstring.inSubStringV0("ADOBECODEBANC", "ABC"))
    print(minSubstring.inSubStringV0("aa", "a"))
    print(minSubstring.inSubStringV0("a", "a"))
    print("***__***")
    print(minSubstring.inSubStringV1("ADOBECODEBANC", "ABC"))
    print(minSubstring.inSubStringV1("aa", "a"))
    print(minSubstring.inSubStringV1("a", "a"))
