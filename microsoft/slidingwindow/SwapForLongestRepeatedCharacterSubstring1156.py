class SwapForLongestRepeatedCharSubstring:

    def maxRepOpt1(self, text: str) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param text:
        :return:
        """

        text += " "
        freqRecorder = {}
        encoded = []
        left, right = 0, 0

        # group repeating characters
        # store the freq
        # add encode the char and length
        while right < len(text):
            if text[right] != text[left]:
                encoded.append([text[left], right - left])
                left = right
            freqRecorder[text[right]] = freqRecorder.get(text[right]) + 1
            right += 1

        maxRep = 0

        # merge sections if we can
        for i in range(len(encoded)):
            # abaaba --> aaaabb
            if i + 2 < len(encoded) and encoded[i + 1][1] == 1 and encoded[i][0] == encoded[i + 2][0]:
                encoded[i][1] += encoded[i + 2][1]
            # abbaa --> aabab, the least we can do when we have extra
            if freqRecorder[encoded[i][0]] > encoded[i][1]:
                encoded[i][1] += 1

            maxRep = max(maxRep, encoded[i][1])
        return maxRep
