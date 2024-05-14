

class MaxRepeatedSubString:

    def swap_for_longest_repeated(self, text: str) -> int:
        """
        Approach: Hash Bucket and Frequency
        T: O(N)
        S: O(N)
        :param text:
        :return:
        """

        # add sentinel to handle edge case
        text += ' '

        # Step 1: Calculate each character freq as well as repeated char length
        char_freq = {}
        encoded = []
        left = 0
        right = 0

        while right < len(text):
            if text[left] != text[right]:
                encoded.append([text[left], right - left])
                left = right
            char_freq[text[right]] = char_freq.get(text[right], 0) + 1
            right += 1

        max_repeat = 0

        for i in range(len(encoded)):

            if i + 2 < len(encoded) and encoded[i][0] == encoded[i + 2][0] and encoded[i + 1][1] == 1:
                encoded[i][1] += encoded[i + 2][1]
            # swap is taking place
            if char_freq[encoded[i][0]] > encoded[i][1]:
                encoded[i][1] += 1
            max_repeat = max(max_repeat, encoded[i][1])
        return max_repeat

