


class RomanToInteger:

    def __init__(self):
        self._roman_map = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

    def roman_to_int(self, s: str) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        digits = 0
        pointer = 0

        while pointer < len(s):

            if pointer + 1 < len(s) and self._roman_map[s[pointer]] < self._roman_map[s[pointer + 1]]:
                digits = digits + (self._roman_map[s[pointer + 1]] - self._roman_map[s[pointer]])
                pointer += 1
            else:
                digits += self._roman_map[s[pointer]]
            pointer += 1
        return digits