class Substring:

    def minimumWindow(self, s: str, t: str) -> str:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param s:
        :param t:
        :return:
        """

        if not s or not t:
            return ""

        freqT = {}

        for char in t:
            freqT[char] = freqT.get(char, 0) + 1

        # to make it optimal we can only focus on characters present in the t by storing the
        # char and index in a separate list
        filteredS = []
        for index, char in enumerate(s):
            if char in freqT:
                filteredS.append((index, char))

        # ideal minimum length
        required = len(freqT)
        left, right, formed = 0, 0, 0
        # track current window char frequency
        windowCharFreq = {}
        # store min length, left and right indices involved
        windowMetaData = float("inf"), None, None

        while right < len(filteredS):

            char = filteredS[right][1]

            windowCharFreq[char] = windowCharFreq.get(char, 0) + 1

            if windowCharFreq[char] == freqT[char]:
                formed += 1

            while left <= right and formed == required:

                char = filteredS[left][1]

                r = filteredS[right][0]
                l = filteredS[left][0]

                if r - l + 1 < windowMetaData[0]:
                    windowMetaData = (r - l + 1, l, r)

                windowCharFreq[char] -= 1

                if windowCharFreq[char] < freqT[char]:
                    formed -= 1
                left += 1
            right += 1
        return "" if windowMetaData[0] == float("inf") else s[windowMetaData[1]: windowMetaData[2] + 1]


if __name__ == "__main__":
    subString = Substring()
    print(subString.minimumWindow("ADOBECODEBANC", "ABC"))
