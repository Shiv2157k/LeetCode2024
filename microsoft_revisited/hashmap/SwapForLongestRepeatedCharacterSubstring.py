from typing import Dict, List, Union


class SwapForLongestRepeatedCharacterSubString:


    def max_repeat_option_1(self, text: str) -> int:
        """
        Approach: HashMap and bucket for length
        T: O(N + M)
        S: O(N)
        :param text:
        :return:
        """

        # sentinel value for boundary
        text += " "

        # Step 1:
        # - We will figure out the frequency of each char
        # - We will also encode the repeated char length
        # pointers for left and right boundary
        left: int = 0
        right: int = 0
        # for encoding the character
        encoded: List[List[Union[str, int]]] = []
        char_freq: Dict[str, int] = {}

        while right < len(text):
            # we will encode
            if text[right] != text[left]:
                encoded.append([text[left], right - left])
                left = right
            char_freq[text[right]] = char_freq.get(text[right], 0) + 1
            right += 1

        # Step 2: We will merge and check max repeated with a single swap
        max_repeat: int = 0

        for i in range(len(encoded)):

            if i + 2 < len(encoded) and encoded[i + 1][1] == 1 and encoded[i][0] == encoded[i + 2][0]:
                encoded[i][1] += encoded[i + 2][1]

            if char_freq[encoded[i][0]] > encoded[i][1]:
                encoded[i][1] += 1

            max_repeat = max(max_repeat, encoded[i][1])
        return max_repeat
