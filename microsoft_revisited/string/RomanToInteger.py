



class RomanToInteger:

    def __init__(self):
        self._romanToIntMap = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

    def romanToInt(self, s: str) -> int:
        """
        Approach:
        T: O()
        S: O()
        :param s:
        :return:
        """

        digits = 0
        pointer = 0

        while pointer < len(s):
            # IX -> 9
            if pointer + 1 < len(s) and self._romanToIntMap[s[pointer]] < self._romanToIntMap[s[pointer + 1]]:
                digits = digits + (self._romanToIntMap[s[pointer + 1]] - self._romanToIntMap[s[pointer]])
                pointer += 2
            else:
                digits += (self._romanToIntMap[s[pointer]])
                pointer += 1
        return digits